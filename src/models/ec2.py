import boto3
from src.utils.reading_from_user import read_nonempty_string

class ec2:
    def __init__(self, session, region):
        """Initialize with a boto3 session."""
        self.session = session
        self.region = region
        self.ec2 = session.client('ec2', region_name=self.region)

    def list_instances(self):
        """List all EC2 instances, grouped by running and stopped."""
        response = self.ec2.describe_instances()
        running_instances = []
        stopped_instances = []

        # Parse instances
        for reservation in response.get('Reservations', []):
            for instance in reservation['Instances']:
                instance_info = {
                    "Instance ID": instance['InstanceId'],
                    "State": instance['State']['Name'],
                    "Type": instance['InstanceType'],
                    "Region": instance['Placement']['AvailabilityZone'],
                    "Launch Time": instance['LaunchTime'].strftime("%Y-%m-%d %H:%M:%S")
                }
                if instance['State']['Name'] == 'running':
                    running_instances.append(instance_info)
                else:
                    stopped_instances.append(instance_info)

        if not running_instances and not stopped_instances:
            print("No EC2 instances detected.")
        else:
            print("\nRunning Instances:")
            for inst in running_instances:
                print(inst)
            print("\nStopped Instances:")
            for inst in stopped_instances:
                print(inst)

    def start_instance(self):
        """Start a specified EC2 instance."""
        self.list_instances()
        instance_id = read_nonempty_string("Enter the Instance ID to start: ")
        try:
            self.ec2.start_instances(InstanceIds=[instance_id])
            print(f"Starting instance {instance_id}...")
        except Exception as e:
            print(f"Error starting instance {instance_id}: {e}")

    def stop_instance(self):
        """Stop a specified EC2 instance."""
        self.list_instances()
        instance_id = read_nonempty_string("Enter the Instance ID to stop: ")
        try:
            self.ec2.stop_instances(InstanceIds=[instance_id])
            print(f"Stopping instance {instance_id}...")
        except Exception as e:
            print(f"Error stopping instance {instance_id}: {e}")

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
