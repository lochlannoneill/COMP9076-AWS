from src.utils.reading_from_user import read_nonempty_string
from tabulate import tabulate
from datetime import datetime

class EC2Controller:
    def __init__(self, resource, client):
        """Initialize with a boto3 session, region, and EC2 client."""
        self.ec2_resource = resource
        self.ec2_client = client

    def list_instances(self):
            """List all EC2 instances, grouped by running and stopped."""
            running_instances = []
            stopped_instances = []

            # Parse instances
            for instance in self.ec2_resource.instances.all():
                instance_info = {
                    "Instance ID": instance.instance_id,
                    "Name": next((tag['Value'] for tag in instance.tags if tag['Key'] == 'Name'), ''),
                    "State": instance.state['Name'],
                    "Type": instance.instance_type,
                    "Region": instance.placement['AvailabilityZone'],
                    "Launch Time": instance.launch_time.strftime("%Y-%m-%d %H:%M:%S")
                }
                if instance.state['Name'] == 'running':
                    running_instances.append(instance_info)
                else:
                    stopped_instances.append(instance_info)

            # Check if there are running instances
            print("\nRunning Instances:")
            if running_instances:
                print(tabulate(running_instances, headers="keys", tablefmt="grid"))
            else:
                print("No running instances detected.")

            # Check if there are stopped instances
            print("\nStopped Instances:")
            if stopped_instances:
                print(tabulate(stopped_instances, headers="keys", tablefmt="grid"))
            else:
                print("No stopped instances detected.")

    def start_instance(self):
        """Start a specified EC2 instance."""
        instance_id = read_nonempty_string("\nEnter the Instance ID to start: ")
        try:
            self.ec2_client.start_instances(InstanceIds=[instance_id])
            print(f"Instance started: '{instance_id}'")
        except Exception as e:
            print(e)

    def stop_instance(self):
        """Stop a specified EC2 instance."""
        instance_id = read_nonempty_string("\nEnter the Instance ID to stop: ")
        try:
            self.ec2_client.stop_instances(InstanceIds=[instance_id])
            print(f"Instance stopped: '{instance_id}'")
        except Exception as e:
            print(e)

    def delete_instance(self):
        """Delete a specified EC2 instance."""
        instance_id = read_nonempty_string("\nEnter the Instance ID to delete: ")
        try:
            self.ec2_client.terminate_instances(InstanceIds=[instance_id])
            print(f"'{instance_id}' deleted.")
        except Exception as e:
            print(e)

    def list_amis(self):
        """List all AMIs from an EC2 instance."""
        instance_id = read_nonempty_string("\nEnter the Instance ID to list associated AMIs: ")
        print(f"Searching associated AMIs of '{instance_id}'...")
        try:
            # Retrieve AMIs that have a tag or description mentioning the instance ID
            images = self.ec2_client.describe_images(
                Filters=[
                    {
                        'Name': 'tag:InstanceId',
                        'Values': [instance_id]
                    }
                ]
            )
            
            # If there are images associated with the instance, print them in tabular format
            if images['Images']:
                headers = ["AMI ID", "Name", "Creation Date"]
                table_data = [
                    [
                        image['ImageId'],
                        image['Name'],
                        # Parse and format the CreationDate string
                        datetime.strptime(image['CreationDate'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")
                    ]
                    for image in images['Images']
                ]
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
            else:
                print(f"No associated AMIs found for instance '{instance_id}'.")
        except Exception as e:
            print(e)

    def create_ami(self):
        """Create an AMI from a specified EC2 instance."""
        instance_id = read_nonempty_string("\nEnter the Instance ID to create AMI from: ")
        ami_name = read_nonempty_string("Enter a name for the AMI: ")
        try:
            response = self.ec2_client.create_image(InstanceId=instance_id, Name=ami_name)
            ami_id = response['ImageId']
            
            # Add a tag with the Instance ID to the new AMI
            self.ec2_client.create_tags(
                Resources=[ami_id],
                Tags=[{'Key': 'InstanceId', 'Value': instance_id}]
            )
            print(f"AMI created: '{ami_id}'")
        except Exception as e:
            print(e)

    def delete_ami(self):
        """Delete a specified AMI."""
        ami_id = read_nonempty_string("\nEnter the AMI ID to delete: ")
        try:
            self.ec2_client.deregister_image(ImageId=ami_id)
            print(f"Deleted AMI: '{ami_id}'")
        except Exception as e:
            print(e)
