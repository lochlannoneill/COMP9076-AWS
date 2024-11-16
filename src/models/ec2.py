from tabulate import tabulate
from datetime import datetime
from src.utils.reading_from_user import read_nonempty_string

class EC2Controller:
    def __init__(self, resource):
        """Initialize with a boto3 session, region, and EC2 resource."""
        self.ec2_resource = resource

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

        # Display running instances
        print("\nRunning Instances:")
        if running_instances:
            print(tabulate(running_instances, headers="keys", tablefmt="pretty"))
        else:
            print("No running instances detected.")

        # Display stopped instances
        print("\nStopped Instances:")
        if stopped_instances:
            print(tabulate(stopped_instances, headers="keys", tablefmt="pretty"))
        else:
            print("No stopped instances detected.")

    def start_instance(self):
        """Start a specified EC2 instance."""
        instance_id = read_nonempty_string("\nEnter the Instance ID to start: ")
        
        # Start instance using resource method
        try:
            instance = self.ec2_resource.Instance(instance_id)
            instance.start()
            print(f"Started '{instance_id}'")
        except Exception as e:
            print(e)

    def stop_instance(self):
        """Stop a specified EC2 instance."""
        instance_id = read_nonempty_string("\nEnter the Instance ID to stop: ")
        
        # Stop instance using resource method
        try:
            instance = self.ec2_resource.Instance(instance_id)
            instance.stop()
            print(f"Stopped '{instance_id}'")
        except Exception as e:
            print(e)

    def delete_instance(self):
        """Delete a specified EC2 instance."""
        instance_id = read_nonempty_string("\nEnter the Instance ID to delete: ")
        
        # Terminate instance using resource method
        try:
            instance = self.ec2_resource.Instance(instance_id)
            instance.terminate()
            print(f"Deleted '{instance_id}'")
        except Exception as e:
            print(e)

    def list_amis(self):
        """List all AMIs from an EC2 instance."""
        instance_id = read_nonempty_string("\nEnter the Instance ID to list associated AMIs: ")
        print(f"Searching associated AMIs of '{instance_id}'...")
        
        # Search for images associated with the instance
        try:
            images = self.ec2_resource.images.filter(Filters=[
                {'Name': 'tag:InstanceId', 'Values': [instance_id]}
            ])
            
            # Display images
            if images:
                headers = ["AMI ID", "Name", "Creation Date"]
                table_data = [
                    [
                        image.id,
                        image.name,
                        image.creation_date.strftime("%Y-%m-%d %H:%M:%S")
                    ]
                    for image in images
                ]
                print(tabulate(table_data, headers=headers, tablefmt="pretty"))
            else:
                print(f"No associated AMIs found for instance '{instance_id}'.")
        except Exception as e:
            print(e)

    def create_ami(self):
        """Create an AMI from a specified EC2 instance."""
        instance_id = read_nonempty_string("\nEnter the Instance ID to create AMI from: ")
        ami_name = read_nonempty_string("Enter a name for the AMI: ")
        
        # Create AMI using resource method
        try:
            instance = self.ec2_resource.Instance(instance_id)
            response = instance.create_image(Name=ami_name)
            ami_id = response.id
            
            # Tag the AMI with the instance ID
            self.ec2_resource.create_tags(
                Resources=[ami_id],
                Tags=[{'Key': 'InstanceId', 'Value': instance_id}]
            )
            print(f"Created AMI '{ami_id}'")
        except Exception as e:
            print(e)

    def delete_ami(self):
        """Delete a specified AMI."""
        ami_id = read_nonempty_string("\nEnter the AMI ID to delete: ")
        
        # Deregister AMI using resource method
        try:
            image = self.ec2_resource.Image(ami_id)
            image.deregister()
            print(f"Deleted AMI '{ami_id}'")
        except Exception as e:
            print(e)
