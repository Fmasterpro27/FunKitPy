import argparse

from .jokes import joke, dad_joke
from .roasts import roast
from .quotes import quote
from importlib.metadata import version


__version__ = version("FunKitPy")


def main():
    parser = argparse.ArgumentParser(
        prog="funkit",
        description="FunKitPy - Random jokes, dad jokes, quotes and roasts",
    )

    parser.add_argument(
        "-v",
        "-V",
        "--version",
        action="store_true",
        help="Show FunKitPy version",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
    )

    subparsers.add_parser(
        "joke",
        help="Get a random joke",
    )

    subparsers.add_parser(
        "dad-joke",
        help="Get a random dad joke",
    )

    subparsers.add_parser(
        "roast",
        help="Get a random roast",
    )

    subparsers.add_parser(
        "quote",
        help="Get a random quote",
    )

    subparsers.add_parser(
        "commands",
        help="List all available commands",
    )

    args = parser.parse_args()

    if args.version:
        print(f"FunKitPy v{__version__}")
        return

    if args.command == "joke":
        print(joke())

    elif args.command == "dad-joke":
        print(dad_joke())

    elif args.command == "roast":
        print(roast())

    elif args.command == "quote":
        print(quote())

    elif args.command == "commands":
        print("""
Available Commands:

  joke         Get a random joke
  dad-joke     Get a random dad joke
  roast        Get a random roast
  quote        Get a random quote
  commands     Show all commands

Flags:

  -v, -V,
  --version    Show version information

Examples:

  funkit joke
  funkit dad-joke
  funkit roast
  funkit quote
  funkit -v
""")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()