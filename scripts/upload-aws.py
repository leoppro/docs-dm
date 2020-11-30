import logging
import boto3
import sys
from botocore.exceptions import ClientError

BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')

def upload_file(file_name, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, BUCKET_NAME, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__ == "__main__":
    local_file = sys.argv[1]
    remote_name = sys.argv[2]
    print(local_file, remote_name)
    upload_file(local_file, remote_name)