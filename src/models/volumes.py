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

    # Other methods (create_volume, attach_volume, etc.) remain the same.
