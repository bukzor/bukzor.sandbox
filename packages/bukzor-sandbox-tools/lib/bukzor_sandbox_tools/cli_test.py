import pytest

from .cli import main


class DescribeMain:
    def it_requires_a_verb(self, capsys: pytest.CaptureFixture[str]):
        with pytest.raises(SystemExit) as exc:
            main([])
        assert exc.value.code == 2, exc.value.code
        assert "VERB" in capsys.readouterr().err

    def it_rejects_an_unknown_verb(self, capsys: pytest.CaptureFixture[str]):
        with pytest.raises(SystemExit) as exc:
            main(["frobnicate"])
        assert exc.value.code == 2, exc.value.code
        assert "frobnicate" in capsys.readouterr().err
