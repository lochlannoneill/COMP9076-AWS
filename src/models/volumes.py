from src.utils.reading_from_user import read_nonnegative_integer, read_nonempty_string
from tabulate import tabulate

class Volumes:
    def __init__(self, ec2_client, ec2_resource):
        """Initialize with a boto3 client and resource for EC2."""
        self.ec2_client = ec2_client
        self.volume_resource = ec2_resource

    def list_volumes(self):
        """List all EBS volumes."""
        in_use_volumes = []
        available_volumes = []

        # Parse volumes
        for volume in self.volume_resource.volumes.all():
            # Gather basic volume info
            volume_info = {
                "Volume ID": volume.volume_id,
                "Size": f"{volume.size} GiB",
                "State": volume.state,
                "Availability Zone": volume.availability_zone
            }

            # Check if volume is attached to an instance and get mount point (device)
            mount_point = "Not Attached"
            if volume.state == "in-use":
                # Retrieve attachments and mount points (mount point)
                for attachment in volume.attachments:
                    instance_id = attachment.get("InstanceId")
                    device = attachment.get("Device")
                    mount_point = f"{device} (Instance: {instance_id})"

            # Update the volume info with mount point if it's in-use
            if volume.state == 'in-use':
                volume_info["Mount Point"] = mount_point
                in_use_volumes.append(volume_info)  # Append only once
            else:
                available_volumes.append(volume_info)  # Append only once

        # Display results in tabular format
        print("\nIn-Use Volumes:")
        if in_use_volumes:
            print(tabulate(in_use_volumes, headers="keys", tablefmt="pretty"))
        else:
            print("No in-use volumes detected.")

        print("Available Volumes:")
        if available_volumes:
            print(tabulate(available_volumes, headers="keys", tablefmt="pretty"))
        else:
            print("No available volumes detected.")
            
    def create_volume(self):
        """Create a new EBS volume."""
        size = read_nonnegative_integer("\nEnter the size of the volume (GiB): ")
        
        # List available zones for the region dynamically
        available_zones = [az['ZoneName'] for az in self.ec2_client.describe_availability_zones()['AvailabilityZones']]
        
        print("Available zones:")
        for idx, az in enumerate(available_zones, start=1):
            print(f"\t{idx}. {az}")
        
        # Get valid availability zone from user input
        az_index = read_nonnegative_integer("Select the Availability Zone by number: ") - 1
        if 0 <= az_index < len(available_zones):
            az = available_zones[az_index]
            
            # Create the volume
            response = self.ec2_client.create_volume(Size=size, AvailabilityZone=az)
            volume_id = response['VolumeId']
            print(f"Volume created: '{volume_id}'")
        else:
            print("Invalid zone selected.")

    def attach_volume(self):
        """Attach a volume to an EC2 instance."""
        volume_id = read_nonempty_string("\nEnter the Volume ID to attach: ")
        instance_id = read_nonempty_string("Enter the Instance ID to attach to: ")  # Ensure this is an EC2 instance ID
        
        # List of mount points  # TODO - get dynamically
        available_devices = ['/dev/sdf', '/dev/sdg', '/dev/sdh', '/dev/sdi', '/dev/sdj', '/dev/sdk']
        
        print("Available mount points:")
        for idx, device in enumerate(available_devices, start=1):
            print(f"\t{idx}. {device}")
        
        device_index = read_nonnegative_integer("Select the mount point by number: ") - 1
        if 0 <= device_index < len(available_devices):
            device = available_devices[device_index]
            
            try:
                response = self.ec2_client.attach_volume(VolumeId=volume_id, InstanceId=instance_id, Device=device)
                print(f"'{volume_id}' {response['State']} to '{instance_id}' at '{device}'")
            except botocore.exceptions.ClientError as e:
                print(f"Error attaching volume: {e}")
        else:
            print("Invalid device selection.")

    def detach_volume(self):
        """Detach a volume from an EC2 instance."""
        volume_id = read_nonempty_string("\nEnter the Volume ID to detach: ")
        response = self.ec2_client.detach_volume(VolumeId=volume_id)
        print(f"'{volume_id}' {response['State']} from '{response['InstanceId']}' at '{response['Device']}'")  # TODO - validation when trying to detach available volume

    def delete_volume(self):
        """Delete a volume."""
        volume_id = read_nonempty_string("\nEnter the Volume ID to delete: ")
        self.ec2_client.delete_volume(VolumeId=volume_id)
        print(f"'{volume_id}' deleted.")
