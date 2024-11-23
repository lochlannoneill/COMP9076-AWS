import os
from pathlib import Path
from src.utils.reading_from_user import read_nonempty_string, read_range_integer

class S3Controller:
    def __init__(self, resource):
        """Initialize with a boto3 resource session."""
        self.s3_resource = resource

    # COMPLETED
    def list_buckets(self):
        """List all S3 buckets."""
        buckets = self.s3_resource.buckets.all()
        
        # Parse buckets
        bucket_info = []
        for bucket in buckets:
            region = bucket.meta.client.get_bucket_location(Bucket=bucket.name)
            bucket_info.append({
                'Name': bucket.name,
                'Region': region['LocationConstraint'],
                'Creation Date': bucket.creation_date.strftime('%Y-%m-%d %H:%M:%S')
            })

        # Display buckets
        print("\nBuckets:")
        if not bucket_info:
            print("\nNo buckets found.")
        else:
            for bucket in bucket_info:
                print(bucket)

    # COMPLETED
    def delete_bucket(self):
        """Delete a bucket after validation."""
        bucket_name = read_nonempty_string("\nEnter bucket name to delete: ")

        # Check if the bucket exists
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            # Check if the bucket is empty
            objects = list(bucket.objects.all())
            if objects:
                # Display objects in the bucket
                print(f"Bucket '{bucket_name}' contains the following objects:")
                for obj in objects:
                    print(f"\t'{obj.key}'")

                # Confirm deletion of all objects
                confirm = input(f"\nDelete all objects in '{bucket_name}' (yes/no): ")
                
                # NO
                if confirm.lower() == 'no':
                    print(f"'{bucket_name}' was not deleted")
                    return
                
                # YES
                for obj in objects:
                    print(f"\tDeleting '{obj.key}'")
                    obj.delete()

            # Delete the bucket
            bucket.delete()
            print(f"Deleted '{bucket_name}'")

        except Exception as e:
            print(f"Unexpected error: {e}")

    # COMPLETED
    def list_objects(self):
        """List all objects in a specified bucket."""
        bucket_name = read_nonempty_string("\nEnter bucket name to list objects: ")
        
        # Check if the bucket exists
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            objects = list(bucket.objects.all())
            
            # Display objects
            if not objects:
                print(f"No objects found in bucket '{bucket_name}'.")
            else:
                print(f"Objects in bucket '{bucket_name}':")
                for obj in objects:
                    print(f"\t{obj.key}")
                
        except Exception as e:
            print(e)

    # COMPLETED
    def upload_object(self):
        """Upload a file to a specified bucket."""
        bucket_name = read_nonempty_string("\nEnter bucket name: ")
        file_name = read_nonempty_string("Enter file to upload: ")

        # Check if the file exists
        if not os.path.isfile(file_name):
            print(f"Error: The file '{file_name}' does not exist.")
            return

        # Upload the file
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            bucket.upload_file(file_name, file_name)  # Uploads file using the same name in the bucket
            print(f"Uploaded '{file_name}' to '{bucket_name}'")
            
        except Exception as e:
            print(f"An error occurred: {e}")

    # COMPLETED
    def download_object(self):
        """Download a file from a specified bucket to the 'Downloads' folder."""
        bucket_name = read_nonempty_string("\nEnter bucket name to download object: ")

        # Check if the bucket exists
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            objects = list(bucket.objects.all())

            # Check if the bucket is empty
            if not objects:
                print(f"Error: No files found in the bucket '{bucket_name}'.")
                return

            # Display files in the bucket
            print(f"Files in bucket '{bucket_name}':")
            for index, obj in enumerate(objects, 1):
                print(f"\t{index}. '{obj.key}'")

            # Get the file to download
            choice = read_range_integer("Enter object index to download: ", 1, len(objects))
            file_name = objects[choice - 1].key

            # Set the download path
            user_home = Path.home()
            downloads_folder = user_home / 'Downloads'
            file_path = downloads_folder / file_name

            # Download the file
            bucket.download_file(file_name, str(file_path))
            print(f"Downloaded '{file_path}'")

        except Exception as e:
            print(f"Error: {e}")
       
    # COMPLETED     
    def delete_object(self):
        """Delete an object from a specified bucket."""
        bucket_name = read_nonempty_string("\nEnter bucket name to delete object: ")

        # Check if the bucket exists
        try:
            bucket = self.s3_resource.Bucket(bucket_name)
            objects = list(bucket.objects.all())

            # Check if the bucket is empty
            if not objects:
                print(f"Error: No objects found in the bucket '{bucket_name}'.")
                return

            # Display objects in the bucket
            print(f"Objects in bucket '{bucket_name}':")
            for index, obj in enumerate(objects, 1):
                print(f"\t{index}. '{obj.key}'")

            # Get the object to delete
            choice = read_range_integer("Enter object index to delete: ", 1, len(objects))
            object_key = objects[choice - 1].key  # Adjust for 0-based index

            # Delete the object
            bucket.Object(object_key).delete()
            print(f"Deleted '{object_key}'")

        except Exception as e:
            print(f"Error: {e}")
