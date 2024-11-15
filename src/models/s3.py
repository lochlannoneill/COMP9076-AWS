import os
from pathlib import Path
from tabulate import tabulate
from src.utils.reading_from_user import read_nonempty_string, read_range_integer

class S3Controller:
    def __init__(self, resource):
        """Initialize with a boto3 resource session."""
        self.s3_resource = resource

    def list_buckets(self):
        """List all S3 buckets."""
        buckets = self.s3_resource.buckets.all()
        
        bucket_info = []
        for bucket in buckets:
            # Fetch region information using the bucket's resource
            region = bucket.meta.client.get_bucket_location(Bucket=bucket.name)
            bucket_info.append({
                'Name': bucket.name,
                'Region': region['LocationConstraint'],
                'Creation Date': bucket.creation_date.strftime('%Y-%m-%d %H:%M:%S')
            })

        print("\nBuckets:")
        if not bucket_info:
            print("\nNo buckets found.")
        else:
            print(tabulate(bucket_info, headers='keys', tablefmt='pretty'))

    def delete_bucket(self):
        """Delete a bucket after validation."""
        bucket_name = read_nonempty_string("\nEnter the bucket name: ")

        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            # Check if the bucket is empty
            objects = list(bucket.objects.all())
            if objects:
                # If there are objects, ask for confirmation to delete them
                print(f"Bucket '{bucket_name}' contains the following objects:")
                for obj in objects:
                    print(f"\t'{obj.key}'")

                # Delete all objects in the bucket
                confirm = input(f"\nDelete all objects in '{bucket_name}' (yes/no): ")
                if confirm.lower() != 'yes':
                    print(f"'{bucket_name}' was not deleted")
                    return
                # NO
                for obj in objects:
                    print(f"\tDeleting '{obj.key}'")
                    obj.delete()

            # Now delete the bucket
            bucket.delete()
            print(f"Deleted '{bucket_name}'")

        except Exception as e:
            print(f"Unexpected error: {e}")

    def list_objects(self):
        """List all objects in a specified bucket."""
        bucket_name = read_nonempty_string("\nEnter the bucket name: ")
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            objects = list(bucket.objects.all())
            if objects:
                print(f"Objects in bucket '{bucket_name}':")
                for obj in objects:
                    print(f"\t{obj.key}")
            else:
                print(f"No objects found in bucket '{bucket_name}'.")
        except Exception as e:
            print(e)

    def upload_object(self):
        """Upload a file to a specified bucket."""
        bucket_name = read_nonempty_string("\nEnter the bucket name: ")
        file_name = read_nonempty_string("Enter the file to upload: ")

        # Check if the file exists
        if not os.path.isfile(file_name):
            print(f"Error: The file '{file_name}' does not exist.")
            return

        try:
            # Get the bucket and upload the file
            bucket = self.s3_resource.Bucket(bucket_name)
            bucket.upload_file(file_name, file_name)  # Uploads file using the same name in the bucket
            print(f"Uploaded '{file_name}' to '{bucket_name}'")
        except Exception as e:
            print(f"An error occurred: {e}")

    def download_object(self):
        """Download a file from a specified bucket to the 'Downloads' folder."""
        bucket_name = read_nonempty_string("\nEnter the bucket name: ")

        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            objects = list(bucket.objects.all())

            # Check if the bucket is empty
            if not objects:
                print(f"Error: No files found in the bucket '{bucket_name}'.")
                return

            # Display the list of objects and give the user a choice
            print(f"Files in bucket '{bucket_name}':")
            for index, obj in enumerate(objects, 1):
                print(f"\t{index}. '{obj.key}'")

            # Get file selection from the user
            choice = read_range_integer("Enter the index of the file to download: ", 1, len(objects))
            file_name = objects[choice - 1].key

            # Get the path to the Downloads folder
            user_home = Path.home()
            downloads_folder = user_home / 'Downloads'
            file_path = downloads_folder / file_name

            # Download the file
            bucket.download_file(file_name, str(file_path))
            print(f"Downloaded '{file_path}'")

        except Exception as e:
            print(f"Error: {e}")
