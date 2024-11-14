from tabulate import tabulate
from src.utils.reading_from_user import read_nonempty_string

class S3Controller:
    def __init__(self, client):
        """Initialize with a boto3 session."""
        self.s3_client = client

    # COMPLETED
    def list_buckets(self):
        """List all S3 buckets."""
        response = self.s3_client.list_buckets()
        
        buckets = []
        for bucket in response['Buckets']:
            region = self.s3_client.get_bucket_location(Bucket=bucket['Name'])
            bucket_info = {
                'Name': bucket['Name'],
                'Region': region['LocationConstraint'],
                'Creation Date': bucket['CreationDate'].strftime('%Y-%m-%d %H:%M:%S')
            }
            buckets.append(bucket_info)

        print("\nBuckets:")
        if not bucket_info:
            print("\nNo buckets found.")
        else:
            print(tabulate(buckets, headers='keys', tablefmt='pretty'))

    # TODO
    # def create_bucket(self):
    #     """Create a new bucket."""
    #     bucket_name = read_nonempty_string("Enter the bucket name: ")
    #     self.s3_client.create_bucket(Bucket=bucket_name)
    #     print(f"Created bucket: {bucket_name}")

    # Completed
    def delete_bucket(self):
        """Delete a bucket after validation."""
        bucket_name = read_nonempty_string("\nEnter the bucket name: ")

        try:
            # Check if the bucket is empty
            objects = self.s3_client.list_objects_v2(Bucket=bucket_name)
            if 'Contents' in objects:
                
                # If there are objects, ask for confirmation to delete them
                print(f"Bucket '{bucket_name}' contains the following objects:")
                for obj in objects['Contents']:
                    print(f"\t'{obj['Key']}'")

                # Delete all objects in the bucket
                confirm = input(f"Delete all objects in '{bucket_name}' (yes/no): ")
                # YES
                if confirm.lower() != 'yes':
                    print("'{bucket_name}' was not deleted")
                    return
                # NO
                for obj in objects['Contents']:
                    print(f"Deleting '{obj['Key']}'")
                    self.s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])

            # Now delete the bucket
            self.s3_client.delete_bucket(Bucket=bucket_name)
            print(f"Deleted '{bucket_name}'")

        except Exception as e:
            print(f"Unexpected error: {e}")

    # TODO
    def list_objects(self):
        """List all objects in a specified bucket."""
        bucket_name = read_nonempty_string("Enter the bucket name: ")
        response = self.s3_client.list_objects_v2(Bucket=bucket_name)
        for obj in response['Contents']:
            print(f"Key: {obj['Key']}")

    # TODO
    def upload_object(self):
        """Upload a file to a specified bucket."""
        bucket_name = read_nonempty_string("Enter the bucket name: ")
        file_path = read_nonempty_string("Enter the file path to upload: ")
        file_name = read_nonempty_string("Enter the file name in S3: ")
        self.s3_client.upload_file(file_path, bucket_name, file_name)
        print(f"Uploaded {file_path} to {bucket_name}/{file_name}")

    # TODO
    def download_object(self):
        """Download a file from a specified bucket."""
        bucket_name = read_nonempty_string("Enter the bucket name: ")
        file_name = read_nonempty_string("Enter the file name in S3: ")
        file_path = read_nonempty_string("Enter the file path to save: ")
        self.s3_client.download_file(bucket_name, file_name, file_path)
        print(f"Downloaded {bucket_name}/{file_name} to {file_path}")

    # TODO
    def delete_object(self):
        """Delete an object from a specified bucket."""
        bucket_name = read_nonempty_string("Enter the bucket name: ")
        object_key = read_nonempty_string("Enter the object key to delete: ")
        self.s3_client.delete_object(Bucket=bucket_name, Key=object_key)
        print(f"Deleted {bucket_name}/{object_key}")
