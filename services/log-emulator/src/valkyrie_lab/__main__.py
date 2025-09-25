"""Command-line interface for Valkyrie Lab."""
from __future__ import annotations

import argparse
from typing import Sequence

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="valkyrie-lab",
        description="Valkyrie Lab reference command-line interface",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Display the Valkyrie Lab version and exit",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        print(f"Valkyrie Lab {__version__}")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
