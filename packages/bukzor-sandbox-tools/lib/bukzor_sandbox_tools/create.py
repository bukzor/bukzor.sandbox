"""`create`: bring new sandboxes into existence, as `mkdir` brings directories
(`docs/dev/claims.kb/design.kb/components.kb/create.md`)."""

import errno
import os
import shlex
import stat
import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path

COLLECTION = "sandbox-repo.kb"


class CreateError(Exception):
    """Why one PATH could not become a sandbox, in `mkdir`'s words where it has them."""


def check_parent(parent: Path, parents: bool) -> None:
    if COLLECTION not in parent.resolve().parts:
        raise CreateError(f"not inside a {COLLECTION}/")
    elif parents:
        parent.mkdir(parents=True, exist_ok=True)
    elif not stat.S_ISDIR(os.stat(parent).st_mode):
        raise CreateError(os.strerror(errno.ENOTDIR))


def exists_on_github(name: str) -> bool:
    """Whether `gh`'s default owner already has a repository `name`. Any failure
    of `gh repo view` reads as absent; `gh repo create` then reports the rest."""
    view = subprocess.run(
        ("gh", "repo", "view", name, "--json", "url"), capture_output=True
    )
    return view.returncode == 0


def create_sandbox(path: Path, parents: bool, visibility: str) -> None:
    """Make the GitHub repository, the record, and the clone for `path`, or
    raise before making any of them."""
    name = path.name
    record = path.parent / f"{name}.md"
    clone = path.parent / f"{name}.git"

    check_parent(path.parent, parents)
    if (
        record.exists(follow_symlinks=False)
        or clone.exists(follow_symlinks=False)
        or exists_on_github(name)
    ):
        raise CreateError(os.strerror(errno.EEXIST))

    url = subprocess.run(
        ("gh", "repo", "create", name, f"--{visibility}"),
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    ).stdout.strip()
    record.write_text(f"---\nurl: {url}\n---\n")
    subprocess.run(("gh", "repo", "clone", name, clone), check=True)


def main(paths: Sequence[Path], parents: bool, visibility: str) -> int:
    status = 0
    for path in paths:
        try:
            create_sandbox(path, parents, visibility)
        except (CreateError, OSError, subprocess.CalledProcessError) as error:
            match error:
                case CreateError():
                    reason = str(error)
                case OSError():
                    reason = error.strerror
                case subprocess.CalledProcessError():
                    command = shlex.join(map(str, error.cmd))
                    reason = f"{command} exited {error.returncode}"
            print(
                f"bukzor-sandbox create: cannot create sandbox '{path}': {reason}",
                file=sys.stderr,
            )
            status = 1
    return status
