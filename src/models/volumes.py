from src.utils.reading_from_user import read_nonnegative_integer, read_nonempty_string

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
            volume_info = {
                "Volume ID": volume.volume_id,
                "Size": f"{volume.size} GiB",
                "State": volume.state,
                "Availability Zone": volume.availability_zone
            }
            if volume.state == 'in-use':
                in_use_volumes.append(volume_info)
            else:
                available_volumes.append(volume_info)

        # Display results in a structured format
        print("\nIn-Use Volumes:")
        if in_use_volumes:
            for vol in in_use_volumes:
                print(vol)
        else:
            print("No in-use volumes detected.")

        print("\nUnused Volumes:")
        if available_volumes:
            for vol in available_volumes:
                print(vol)
        else:
            print("No unused volumes detected.")

    def create_volume(self):
        """Create a new EBS volume."""
        size = read_nonnegative_integer("Enter the size of the volume (GiB): ")
        az = read_nonempty_string("Enter the Availability Zone: ")
        response = self.ec2.create_volume(Size=size, AvailabilityZone=az)
        print(f"Volume created: {response['VolumeId']}")

    def attach_volume(self):
        """Attach a volume to an EC2 instance."""
        volume_id = read_nonempty_string("Enter the Volume ID to attach: ")
        instance_id = read_nonempty_string("Enter the Instance ID to attach to: ")
        device = read_nonempty_string("Enter the device name (e.g., /dev/sdf): ")
        response = self.ec2.attach_volume(VolumeId=volume_id, InstanceId=instance_id, Device=device)
        print(f"Volume attached: {response['State']}")

    def detach_volume(self):
        """Detach a volume from an EC2 instance."""
        volume_id = read_nonempty_string("Enter the Volume ID to detach: ")
        response = self.ec2.detach_volume(VolumeId=volume_id)
        print(f"Volume detached: {response['State']}")

    def delete_volume(self):
        """Delete a volume."""
        volume_id = read_nonempty_string("Enter the Volume ID to delete: ")
        self.ec2.delete_volume(VolumeId=volume_id)
        print(f"Deleted volume: {volume_id}")
