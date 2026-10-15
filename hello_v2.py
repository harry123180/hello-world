"""hello-world v2 — a small but more capable CLI greeting tool.

Compared with v1 (`hello.py`), this version adds:

* command-line arguments instead of hard-coded behaviour
* a configurable greeting and repeat count
* optional UPPERCASE ("shout") output
* a `--version` flag and sensible exit codes

Usage:
    python hello_v2.py
    python hello_v2.py Alice
    python hello_v2.py Alice Bob --greeting Hi --count 2
    python hello_v2.py World --shout
"""

from __future__ import annotations

import argparse
import sys
from typing import Iterable, Sequence

__version__ = "2.0.0"

DEFAULT_GREETING = "Hello"
DEFAULT_NAMES: tuple[str, ...] = ("World",)


def greet(
    names: Iterable[str] = DEFAULT_NAMES,
    greeting: str = DEFAULT_GREETING,
    count: int = 1,
    shout: bool = False,
) -> list[str]:
    """Build one greeting line per name.

    Args:
        names: People (or things) to greet. Empty or blank entries are skipped.
        greeting: Word placed before the name, e.g. "Hello".
        count: How many times to repeat each greeting. Must be >= 1.
        shout: Uppercase the whole line when True.

    Returns:
        A list of greeting lines.

    Raises:
        ValueError: If `count` is less than 1.
    """
    if count < 1:
        raise ValueError("count must be at least 1")

    lines: list[str] = []
    for name in names:
        target = name.strip()
        if not target:
            continue
        line = f"{greeting}, {target}!"
        lines.extend([line.upper() if shout else line] * count)
    return lines


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog="hello_v2",
        description="Greet one or more people from the command line.",
    )
    parser.add_argument(
        "names",
        nargs="*",
        default=list(DEFAULT_NAMES),
        metavar="NAME",
        help="who to greet (default: World)",
    )
    parser.add_argument(
        "-g",
        "--greeting",
        default=DEFAULT_GREETING,
        help="greeting word to use (default: Hello)",
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=1,
        help="repeat each greeting this many times (default: 1)",
    )
    parser.add_argument(
        "-s",
        "--shout",
        action="store_true",
        help="uppercase the output",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI. Returns a process exit code."""
    args = build_parser().parse_args(argv)

    try:
        lines = greet(args.names, greeting=args.greeting, count=args.count, shout=args.shout)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if not lines:
        print("error: no names to greet", file=sys.stderr)
        return 2

    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
