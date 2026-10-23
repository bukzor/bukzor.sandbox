from pathlib import Path

import pytest

from .cli import main

# Stands in for `gh`: a repository exists on "GitHub" iff its directory exists
# under $FAKE_GH/repos, and every invocation is appended to $FAKE_GH/log.
FAKE_GH = """\
#!/bin/bash
set -eu
echo "$*" >> "$FAKE_GH/log"
case "$1 $2" in
  "repo view") test -d "$FAKE_GH/repos/$3" ;;
  "repo create")
    if [ "$3" = rejected ]; then exit 1; fi
    mkdir "$FAKE_GH/repos/$3"; echo "https://github.com/someone/$3" ;;
  "repo clone") mkdir "$4" ;;
  *) exit 99 ;;
esac
"""


class FakeGitHub:
    def __init__(self, root: Path):
        self.root = root
        (root / "repos").mkdir(parents=True)
        (root / "log").touch()

    def add(self, name: str):
        (self.root / "repos" / name).mkdir()

    def calls(self):
        return (self.root / "log").read_text().splitlines()


@pytest.fixture
def github(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    bin = tmp_path / "bin"
    bin.mkdir()
    gh = bin / "gh"
    gh.write_text(FAKE_GH)
    gh.chmod(0o755)
    monkeypatch.setenv("PATH", f"{bin}:/usr/bin:/bin")
    monkeypatch.setenv("FAKE_GH", str(tmp_path / "github"))
    return FakeGitHub(tmp_path / "github")


@pytest.fixture
def parent(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """A parent repo's working directory, holding an empty `sandbox-repo.kb/`."""
    root = tmp_path / "parent"
    (root / "sandbox-repo.kb").mkdir(parents=True)
    monkeypatch.chdir(root)
    return root


def create(*argv: str):
    return main(["create", *argv])


class DescribeCreate:
    def it_creates_the_repository_the_record_and_the_clone(
        self, github: FakeGitHub, parent: Path
    ):
        assert create("--private", "sandbox-repo.kb/opus") == 0
        assert "repo create opus --private" in github.calls(), github.calls()
        record = parent / "sandbox-repo.kb/opus.md"
        assert record.read_text() == "---\nurl: https://github.com/someone/opus\n---\n"
        assert (parent / "sandbox-repo.kb/opus.git").is_dir()

    def it_requires_a_visibility(self, capsys: pytest.CaptureFixture[str]):
        with pytest.raises(SystemExit) as exc:
            create("sandbox-repo.kb/opus")
        assert exc.value.code == 2, exc.value.code
        assert "--public --private --internal" in capsys.readouterr().err

    def it_proceeds_past_a_failed_path_and_exits_1(
        self, github: FakeGitHub, parent: Path
    ):
        (parent / "sandbox-repo.kb/taken.md").touch()
        assert create("--public", "sandbox-repo.kb/taken", "sandbox-repo.kb/b") == 1
        assert (parent / "sandbox-repo.kb/b.git").is_dir()

    def it_reports_a_failed_gh_command(
        self,
        github: FakeGitHub,
        parent: Path,
        capsys: pytest.CaptureFixture[str],
    ):
        assert create("--private", "sandbox-repo.kb/rejected") == 1
        assert capsys.readouterr().err.endswith(
            "'sandbox-repo.kb/rejected': gh repo create rejected --private exited 1\n"
        )

    class WhenTheSandboxExists:
        @pytest.mark.parametrize("entry", ["opus.md", "opus.git"])
        def it_fails_with_file_exists_on_disk(
            self,
            github: FakeGitHub,
            parent: Path,
            capsys: pytest.CaptureFixture[str],
            entry: str,
        ):
            (parent / "sandbox-repo.kb" / entry).mkdir()
            assert create("--private", "sandbox-repo.kb/opus") == 1
            assert capsys.readouterr().err == (
                "bukzor-sandbox create: cannot create sandbox"
                " 'sandbox-repo.kb/opus': File exists\n"
            )
            assert github.calls() == [], github.calls()

        def it_fails_with_file_exists_on_github(
            self,
            github: FakeGitHub,
            parent: Path,
            capsys: pytest.CaptureFixture[str],
        ):
            github.add("opus")
            assert create("--private", "sandbox-repo.kb/opus") == 1
            assert "opus': File exists\n" in capsys.readouterr().err
            assert github.calls() == ["repo view opus --json url"], github.calls()
            assert list((parent / "sandbox-repo.kb").iterdir()) == []

    class WhenTheParentDirectoryIsMissing:
        def it_fails_with_no_such_file_or_directory(
            self,
            github: FakeGitHub,
            parent: Path,
            capsys: pytest.CaptureFixture[str],
        ):
            assert create("--private", "sandbox-repo.kb/graphics/opus") == 1
            assert capsys.readouterr().err.endswith(
                "'sandbox-repo.kb/graphics/opus': No such file or directory\n"
            )
            assert github.calls() == [], github.calls()

        def it_creates_it_given_parents(self, github: FakeGitHub, parent: Path):
            assert create("-p", "--private", "sandbox-repo.kb/graphics/opus") == 0
            assert (parent / "sandbox-repo.kb/graphics/opus.md").is_file()

    class WhenThePathIsOutsideTheCollection:
        def it_fails_and_makes_nothing(
            self,
            github: FakeGitHub,
            parent: Path,
            capsys: pytest.CaptureFixture[str],
        ):
            assert create("--private", "opus") == 1
            assert capsys.readouterr().err.endswith(
                "'opus': not inside a sandbox-repo.kb/\n"
            )
            assert github.calls() == [], github.calls()
