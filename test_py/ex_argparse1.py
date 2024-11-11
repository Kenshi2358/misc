"""
Argparse example:
You cannot use optional functionl parameters for an argparse parameter that is not filled out.
The non-filled out argparse parameter defaults to None. None gets passed to the function and stays as None.
None type is still an object type according to argparse.

To correct, use argparses's default option when it's not being used.
For example:
parser.add_argument("-e", "--encoding", type=str, help="File encoding", required=False)
"""
import argparse
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)


def filewrite(encoding='utf-8'):

    logging.info(f'Encoding type: {encoding}')


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-e", "--encoding", type=str, help="File encoding", required=False)
    parser.add_argument('-r', "--recipients", type=str, help="email recipients")
    parser.add_argument('-s', "--server", type=str, help="server name")
    parser.add_argument('-d', "--database", type=str, help="database name")
    return parser.parse_args()


def main():
    args = parse_arguments()
    filewrite(encoding=args.encoding)


if __name__ == '__main__':
    main()
