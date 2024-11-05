import boto3
from reading_from_user import read_nonempty_string

class Resource:
    def __init__(self, session):
        """Initialize with a boto3 session."""
        self.ec2 = session.resource('ec2')
        self.s3 = session.resource('s3')

    def list_instances(self):
        """List all EC2 instances."""
        for instance in self.ec2.instances.all():
            print(f"Instance ID: {instance.id}")
            print(f"State: {instance.state['Name']}")
            print(f"Type: {instance.instance_type}")
            print(f"Region: {instance.placement['AvailabilityZone']}")
            print(f"Launch Time: {instance.launch_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print()

    def list_volumes(self):
        """List all EBS volumes."""
        for volume in self.ec2.volumes.all():
            print(f"Volume ID: {volume.id}")
            print(f"Size: {volume.size} GiB")
            print(f"State: {volume.state}")
            print(f"Availability Zone: {volume.availability_zone}")
            print()

    def list_buckets(self):
        """List all S3 buckets."""
        for bucket in self.s3.buckets.all():
            print(f"Bucket: {bucket.name}")

    def list_objects(self):
        """List all objects in a specified bucket."""
        bucket_name = read_nonempty_string("Enter the bucket name: ")
        bucket = self.s3.Bucket(bucket_name)
        for obj in bucket.objects.all():
            print(f"Key: {obj.key}")

    def create_volume(self):
        """Create a new EBS volume."""
        size = int(read_nonempty_string("Enter the size of the volume (GiB): "))
        az = read_nonempty_string("Enter the Availability Zone: ")
        volume = self.ec2.create_volume(Size=size, AvailabilityZone=az)
        print(f"Volume created: {volume.id}")

    def create_bucket(self):
        """Create a new bucket."""
        bucket_name = read_nonempty_string("Enter the bucket name: ")
        bucket = self.s3.create_bucket(Bucket=bucket_name)
        print(f"Created bucket: {bucket.name}")

    def delete_bucket(self):
        """Delete a bucket."""
        bucket_name = read_nonempty_string("Enter the bucket name: ")
        bucket = self.s3.Bucket(bucket_name)
        bucket.delete()
        print(f"Deleted bucket: {bucket_name}")

    def start_instance(self):
        """Start a specified EC2 instance."""
        instance_id