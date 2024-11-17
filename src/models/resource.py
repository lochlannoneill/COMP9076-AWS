import boto3
class Resource:
    def __init__(self, region, user_credentials):
        """Initialize the session with AWS credentials and region."""
        self.region = region
        self.key_id = user_credentials["access_key"]
        self.secret_key = user_credentials["secret_key"]

    def get_ec2_resource(self):
        # Create and return a Resource for interacting with EC2 instances
        try:
            ec2 = boto3.resource("ec2",
                                aws_access_key_id=self.key_id,
                                aws_secret_access_key=self.secret_key,
                                region_name=self.region)
            return ec2
        except Exception as e:
            print(e)
            return None

    def get_s3_resource(self):
        # Create and return a Resource for interacting with S3
        try:
            s3 = boto3.resource("s3",
                                aws_access_key_id=self.key_id,
                                aws_secret_access_key=self.secret_key,
                                region_name=self.region)
            return s3
        except Exception as e:
            print(e)
            return None

    def get_cw_client(self):  # TODO - change to resource
        # Create and return a Client for interacting with CloudWatch
        try:
            cw = boto3.client('cloudwatch',
                            aws_access_key_id=self.key_id,
                            aws_secret_access_key=self.secret_key,
                            region_name=self.region)
            return cw
        except Exception as e:
            print(e)
            return None

    def get_dynamodb_resource(self):
        # Create and return a Resource for interacting with DynamoDB
        try:
            dynamodb = boto3.resource(
                "dynamodb",
                aws_access_key_id=self.key_id,
                aws_secret_access_key=self.secret_key,
                region_name=self.region
            )
            return dynamodb
        except Exception as e:
            print(e)
            return None
