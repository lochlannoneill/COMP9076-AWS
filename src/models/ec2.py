import boto3
from utils.reading_from_user import read_nonempty_string

class ec2:
    def __init__(self, session, region):
        """Initialize with a boto3 session."""
        self.session = session
        self.region = region
        self.ec2 = session.resource('ec2', region_name=self.region)


    def list_instances(self):
        """List all EC2 instances, grouped by running and stopped."""
        response = self.ec2.describe_instances()
        instances = {"running": [], "stopped": []}

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_info = {
                    "Instance ID": instance['InstanceId'],
                    "State": instance['State']['Name'],
                    "Type": instance['InstanceType'],
                    "Region": instance['Placement']['AvailabilityZone'],
                    "Launch Time": instance['LaunchTime'].strftime("%Y-%m-%d %H:%M:%S")
                }
                instances[instance['State']['Name']].append(instance_info)

        print("\nRunning Instances:")
        for inst in instances['running']:
            print(inst)

        print("\nStopped Instances:")
        for inst in instances['stopped']:
            print(inst)

    def start_instance(self):
        """Start a specified EC2 instance."""
        self.list_instances()
        instance_id = read_nonempty_string("Enter the Instance ID to start: ")
        instance = self.ec2.Instance(instance_id)
        instance.start()
        print(f"Starting instance {instance_id}...")

    def stop_instance(self):
        """Stop a specified EC2 instance."""
        self.list_instances()
        instance_id = read_nonempty_string("Enter the Instance ID to stop: ")
        instance = self.ec2.Instance(instance_id)
        instance.stop()
        print(f"Stopping instance {instance_id}...")

    def create_ami(self):
        """Create an AMI from a specified EC2 instance."""
        instance_id = read_nonempty_string("Enter the Instance ID to create AMI from: ")
        ami_name = read_nonempty_string("Enter a name for the AMI: ")
        response = self.ec2.create_image(InstanceId=instance_id, Name=ami_name)
        print(f"AMI created: {response['ImageId']}")

    def delete_ami(self):
        """Delete a specified AMI."""
        ami_id = read_nonempty_string("Enter the AMI ID to delete: ")
        self.ec2.deregister_image(ImageId=ami_id)
        print(f"Deleted AMI: {ami_id}")

    def add_tags(self, instance_id, tags):
        instance = self.ec2.Instance(instance_id)
        instance.create_tags(Tags=tags)
        print(f"Tags added to instance {instance_id}")

    def delete_tags(self, instance_id, tags):
        instance = self.ec2.Instance(instance_id)
        instance.delete_tags(Tags=tags)
        print(f"Tags removed from instance {instance_id}")