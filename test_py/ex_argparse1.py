'''
Example of why using argparse with optional function parameters does not work.
The function fails to convert encoding to "utf-8" because None type is still an object type according to argparse.

To correct, use argparses's default option when its not being used.

'''
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
