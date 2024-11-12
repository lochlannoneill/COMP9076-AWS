import boto3
from src.utils.reading_from_user import read_nonempty_string

class EC2Controller:
    def __init__(self, resource):
        """Initialize with a boto3 session and region."""
        self.ec2 = resource

    # COMPLETED
    def list_instances(self):
        """List all EC2 instances, grouped by running and stopped."""
        running_instances = []
        stopped_instances = []

        # Parse instances
        for instance in self.ec2.instances.all():
            instance_info = {
                "Instance ID": instance.instance_id,  # Corrected this line
                "State": instance.state['Name'],  # Corrected this line
                "Type": instance.instance_type,  # Corrected this line
                "Region": instance.placement['AvailabilityZone'],  # Corrected this line
                "Launch Time": instance.launch_time.strftime("%Y-%m-%d %H:%M:%S")
            }
            if instance.state['Name'] == 'running':
                running_instances.append(instance_info)
            else:
                stopped_instances.append(instance_info)

        # Check if there are no instances
        if not running_instances and not stopped_instances:
            print("No EC2 instances detected.")
        else:
            print("\nRunning Instances:")
            if running_instances:
                for inst in running_instances:
                    print(inst)
            else:
                print("No running instances detected.")

            print("\nStopped Instances:")
            if stopped_instances:
                for inst in stopped_instances:
                    print(inst)
            else:
                print("No stopped instances detected.")

    # TODO
    def start_instance(self):
        """Start a specified EC2 instance."""
        instance_id = read_nonempty_string("Enter the Instance ID to start: ")
        try:
            self.ec2.start_instances(InstanceIds=[instance_id])
            print(f"Starting instance {instance_id}...")
        except Exception as e:
            print(f"Error starting instance {instance_id}: {e}")

    # TODO
    def stop_instance(self):
        """Stop a specified EC2 instance."""
        instance_id = read_nonempty_string("Enter the Instance ID to stop: ")
        try:
            self.ec2.stop_instances(InstanceIds=[instance_id])
            print(f"Stopping instance {instance_id}...")
        except Exception as e:
            print(f"Error stopping instance {instance_id}: {e}")

    # TODO
    def create_ami(self):
        """Create an AMI from a specified EC2 instance."""
        instance_id = read_nonempty_string("Enter the Instance ID to create AMI from: ")
        ami_name = read_nonempty_string("Enter a name for the AMI: ")
        response = self.ec2.create_image(InstanceId=instance_id, Name=ami_name)
        print(f"AMI created: {response['ImageId']}")

    # TODO
    def delete_ami(self):
        """Delete a specified AMI."""
        ami_id = read_nonempty_string("Enter the AMI ID to delete: ")
        self.ec2.deregister_image(ImageId=ami_id)
        print(f"Deleted AMI: {ami_id}")
