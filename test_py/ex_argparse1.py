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


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--encoding", type=str, help="File encoding", required=False)
    args = parser.parse_args()
    filewrite(encoding=args.encoding)
