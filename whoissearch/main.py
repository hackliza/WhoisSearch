import argparse
import os
from pathlib import Path

from whoissearch.searcher import Searcher


def main():
    parser = argparse.ArgumentParser(
        description="Get network blocks from whois from a list of words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "white_list",
        metavar='Whitelist',
        type=str,
        help="Indicates the whitelist string or file with lines to process.",
        nargs="+"
    )
    parser.add_argument(
        "-b",
        "--black",
        help="Indicates the blacklist string or file with lines to process.",
        required=False,
        dest="black_list",
        nargs="+"
    )
    parser.add_argument(
        "-n",
        "--not-download",
        help="Indicates that you do not want to download the databases",
        required=False,
        action="store_false",
        default=True,
        dest="download"
    )
    parser.add_argument(
        "-d",
        "--db-dir",
        help="Indicates the read/download directory of databases",
        required=False,
        default=os.path.join(str(Path.home()), ".whoissearch_dbs"),
        dest="db_dir"
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Indicates the output directory",
        required=False,
        default="./whoissearch_results",
        dest="output_directory"
    )
    args = parser.parse_args()

    Searcher().search_networks(args.white_list, args.black_list, args.download, args.db_dir, args.output_directory)


if __name__ == '__main__':
    main()
