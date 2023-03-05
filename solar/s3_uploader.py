import boto3
from botocore.exceptions import ClientError


class S3Uploader:
    """
    Class that handles the upload of a file to an S3 bucket.
    Args:
        bucket_name: the name of the AWS S3 bucket to where a file will be uploaded to.
    """

    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3')

    def upload_file(self, file, file_name):
        """
        Uploads file to AWS S3 Bucket

        :param file: the object that is the file
        :param file_name: the name of the file will be stored in the bucket

        """
        try:
            response = self.s3.upload_fileobj(
                file, self.bucket_name, Key=file_name)
        except ClientError as e:
            print("Error: " + str(e))
