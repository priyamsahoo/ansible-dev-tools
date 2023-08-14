"""Parse the command line arguments."""
import argparse

from .version_builder import version_builder


def parse() -> argparse.Namespace:
    """Parse the command line arguments.

    :returns: The arguments
    """
    parser = argparse.ArgumentParser(
        description="The ansible content development kit.",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="version",
        version=version_builder(),
        help="Print ansible-creator version and exit.",
    )

    return parser.parse_args()
