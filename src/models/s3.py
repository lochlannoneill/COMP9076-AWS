import boto3
from src.utils.reading_from_user import read_nonempty_string

class s3:
    def __init__(self, session):
        """Initialize with a boto3 session."""
        self.s3 = session.client('s3')

    def list_buckets(self):
        """List all S3 buckets."""
        response = self.s3.list_buckets()
        for bucket in response['Buckets']:
            print(f"Bucket: {bucket['Name']}")

    def list_objects(self):
        """List all objects in a specified bucket."""
        bucket_name = read_nonempty_string("Enter the bucket name: ")
        response = self.s3.list_objects_v2(Bucket=bucket_name)
        for obj in response['Contents']:
            print(f"Key: {obj['Key']}")

    def upload_file(self):
        """Upload a file to a specified bucket."""
        bucket_name = read_nonempty_string("Enter the bucket name: ")
        file_path = read_nonempty_string("Enter the file path to upload: ")
        file_name = read_nonempty_string("Enter the file name in S3: ")
        self.s3.upload_file(file_path, bucket_name, file_name)
        print(f"Uploaded {file_path} to {bucket_name}/{file_name}")

    def download_file(self):
        """Download a file from a specified bucket."""
        bucket_name = read_nonempty_string("Enter the bucket name: ")
        file_name = read_nonempty_string("Enter the file name in S3: ")
        file_path = read_nonempty_string("Enter the file path to save: ")
        self.s3.download_file(bucket_name, file_name, file_path)
        print(f"Downloaded {bucket_name}/{file_name} to {file_path}")

    def delete_object(self):
        """Delete an object from a specified bucket."""
        bucket_name = read_nonempty_string("Enter the bucket name: ")
        object_key = read_nonempty_string("Enter the object key to delete: ")
        self.s3.delete_object(Bucket=bucket_name, Key=object_key)
        print(f"Deleted {bucket_name}/{object_key}")

    def create_bucket(self):
        """Create a new bucket."""
        bucket_name = read_nonempty_string("Enter the bucket name: ")
        self.s3.create_bucket(Bucket=bucket_name)
        print(f"Created bucket: {bucket_name}")

    def delete_bucket(self):
        """Delete a bucket."""
        bucket_name = read_nonempty_string("Enter the bucket name: ")
        self.s3.delete_bucket(Bucket=bucket_name)
        print(f"Deleted bucket: {bucket_name}")

    def list_bucket_policy(self):
        """List the bucket policy of a specified bucket."""
        bucket_name = read_nonempty_string("Enter the bucket name: ")
        response = self.s3.get_bucket_policy(Bucket=bucket_name)
        print(f"Bucket policy: {response['Policy']}")
        
        