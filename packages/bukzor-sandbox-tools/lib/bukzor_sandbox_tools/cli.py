"""The parent's one script. Each subcommand is a verb from the design record
(`docs/dev/claims.kb/design.kb/components.kb/`); a verb joins here when its
claim drops `todo: true`."""

import argparse
from collections.abc import Sequence
from pathlib import Path

from . import create


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="bukzor-sandbox",
        description="Operate the sandboxes bound to this parent repo.",
    )
    verbs = parser.add_subparsers(dest="verb", required=True, metavar="VERB")

    create_ = verbs.add_parser(
        "create", help="bring new sandboxes into existence, as mkdir does directories"
    )
    create_.add_argument(
        "-p", "--parents", action="store_true", help="make parent directories as needed"
    )
    visibility = create_.add_mutually_exclusive_group(required=True)
    for choice in ("public", "private", "internal"):
        visibility.add_argument(
            f"--{choice}", dest="visibility", action="store_const", const=choice
        )
    create_.add_argument("paths", nargs="+", type=Path, metavar="PATH")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    match args.verb:
        case "create":
            return create.main(args.paths, args.parents, args.visibility)
        case _:
            raise AssertionError(args.verb)
