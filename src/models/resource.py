import boto3
class Resource:
    def __init__(self, region, key_id, secret_key):
        """Initialize the session with AWS credentials and region."""
        self.session = boto3.Session(
            aws_access_key_id=key_id,
            aws_secret_access_key=secret_key,
            region_name=region
        )

    def _create_resource(self, service_name):
        """Create and return a resource for the specified AWS service."""
        try:
            return self.session.resource(service_name)
        except Exception as e:
            print(f"Error creating resource for {service_name}: {e}")
            return None

    def _create_client(self, service_name):
        """Create and return a client for the specified AWS service."""
        try:
            return self.session.client(service_name)
        except Exception as e:
            print(f"Error creating client for {service_name}: {e}")
            return None

    def get_ec2_resource(self):
        """Get the EC2 resource."""
        return self._create_resource("ec2")
    
    def get_volume_resource(self):
        """Get the volume resource."""
        return self._create_resource("ec2")

    def get_s3_resource(self):
        """Get the S3 resource."""
        return self._create_resource("s3")

    def get_cloudwatch_client(self):
        """Get the CloudWatch client."""
        return self._create_client("cloudwatch")
