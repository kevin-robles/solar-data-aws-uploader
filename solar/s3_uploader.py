import boto3
from botocore.exceptions import ClientError


class S3Uploader:

    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3')

    def upload_file(self, file, file_name):
        try:
            response = self.s3.upload_fileobj(
                file, self.bucket_name, Key=file_name)
        except ClientError as e:
            print("Error: " + str(e))
