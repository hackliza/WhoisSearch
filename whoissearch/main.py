import argparse

from whoissearch.searcher import Searcher


def main():
    parser = argparse.ArgumentParser(
        description="Get network blocks from whois from a list of words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("white_list", metavar='Whitelist', type=str, help="Indicates the whitelist path")
    parser.add_argument("-b", "--black", help="Indicates the blacklist path", required=False, dest="black_list")
    args = parser.parse_args()

    Searcher().search_networks(args.white_list, args.black_list)


if __name__ == '__main__':
    main()
