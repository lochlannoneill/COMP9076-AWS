import boto3
from src.utils.reading_from_user import read_nonempty_string

class resource:
    def __init__(self):
        """Initialize with optional AWS credentials and region."""
        self.region = "eu-west-1"
        self.key_id = "insert here"  # TODO
        self.secret_key = "insert here"  # TODO

    def EC2Resource(self):
        # Create and return a Resource for interacting with EC2 instances
        ec2 = boto3.resource("ec2",aws_access_key_id=self.key_id,
                     aws_secret_access_key=self.secret_key,
                     region_name=self.region)
        return ec2 


    def S3Resource(self):
        # Create and return a Resource for interacting with S3 instances
        s3 = boto3.resource("s3",aws_access_key_id=self.key_id,
                     aws_secret_access_key=self.secret_key,
                     region_name=self.region)
        return s3

    def CWClient(self):
        # Create and return a Client for interacting with CloudWatch
        cw = cloudwatch = boto3.client('cloudwatch',aws_access_key_id=self.key_id,
                     aws_secret_access_key=self.secret_key,
                     region_name=self.region)
        return cw




