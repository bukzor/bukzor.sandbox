"""The parent's one script. Each subcommand is a verb from the design record
(`docs/dev/claims.kb/design.kb/components.kb/`); a verb joins here when its
claim drops `todo: true`."""

import argparse
from collections.abc import Sequence


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="bukzor-sandbox",
        description="Operate the sandboxes bound to this parent repo.",
    )
    parser.add_subparsers(dest="verb", required=True, metavar="VERB")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    raise AssertionError(args.verb)
