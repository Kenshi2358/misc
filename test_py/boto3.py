"""
Works:
python3 ex_boto3.py --file "dummy_file1.txt" --s3_bucket "mdx-des" --s3_file "dummy_file1.txt" --task "u"
python3 ex_boto3.py --file "dummy_file1.txt" --s3_bucket "mdx-des"--s3_file "folder1/dummy_file1.txt" --task "u"
"""

import boto3
import argparse
import logging
import fnmatch

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

s3 = boto3.client('s3')


def upload(local_file, bucket, s3_file):
    print(f"Uploading {local_file} to {bucket} as {s3_file} \n")
    s3.upload_file(local_file, bucket, s3_file)


def download(local_file, bucket, s3_file):
    print(f"Downloading {s3_file} from {bucket} \n")
    s3.download_file(bucket, s3_file, local_file)


def s3_list_contents(args):
    """
    Print out all contents in this bucket as an additional check.
    """

    s3_client = boto3.client('s3')

    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=args.s3_bucket, StartAfter='folder1/folder2/', Prefix='folder1/folder2/')

    my_s3_file_list = []

    # each_response is a dictionary with a number of fields.
    # The contents key contains metadata about each object, which in turn has a Key field containing the filename.
    for each_response in pages:
        for each_object in each_response['Contents']:
            # if each_object['Key'].find('*.zip') >= 0:
            if fnmatch.fnmatch(each_object['Key'], '*.zip'):
                my_s3_file_list.append(each_object["Key"])

    logging.info(f'All contents in s3 folder: {my_s3_file_list}')


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file', help='local file name', required=True)
    parser.add_argument("-s", "--s3_bucket", help='bucket location', required=True)
    parser.add_argument('--s3_file', help='file name on s3', required=True)
    parser.add_argument('--task', help='(u) for upload (d) for download', choices=['u', 'd'], required=True)

    args = parser.parse_args()

    s3_list_contents(args)

    local_file = args.file
    bucket = args.s3_bucket
    s3_file = args.s3_file
    task = args.task

    '''
    #Call function based off of task
    if task == "u":
        call_task = eval("upload")
    elif task =="d":
        call_task = eval("download")

    call_task(local_file=local_file, bucket=s3_bucket, s3_file=s3_file)
    '''


if __name__ == '__main__':
    main()
