import boto3
from src.utils.reading_from_user import read_nonempty_string

class resource:
    def __init__(self, region, key_id, secret_key):
        """Initialize with AWS credentials and region."""
        self.region = region
        self.key_id = key_id
        self.secret_key = secret_key

    # COMPLETED
    def _create_resource(self, service_name):
        """Create and return a resource for the specified AWS service."""
        try:
            return boto3.resource(
                service_name,
                aws_access_key_id=self.key_id,
                aws_secret_access_key=self.secret_key,
                region_name=self.region
            )
        except Exception as e:
            print(f"Error creating resource for {service_name}: {e}")
            return None

    # COMPLETED
    def _create_client(self, service_name):
        """Create and return a client for the specified AWS service."""
        try:
            return boto3.client(
                service_name,
                aws_access_key_id=self.key_id,
                aws_secret_access_key=self.secret_key,
                region_name=self.region
            )
        except Exception as e:
            print(f"Error creating client for {service_name}: {e}")
            return None

    # COMPLETED
    def get_ec2_resource(self):
        """Get the EC2 resource."""
        return self._create_resource("ec2")

    # TODO
    def get_s3_resource(self):
        """Get the S3 resource."""
        return self._create_resource("s3")

    # TODO
    def get_cloudwatch_client(self):
        """Get the CloudWatch client."""
        return self._create_client("cloudwatch")
