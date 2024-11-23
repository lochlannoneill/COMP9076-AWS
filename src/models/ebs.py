import botocore
from src.utils.reading_from_user import read_nonnegative_integer, read_nonempty_string, read_range_integer

class EBSController:
    def __init__(self, resource):
        """Initialize with a boto3 resource for EC2."""
        self.resource = resource
        self.client = resource.meta.client

    # COMPLETED
    def list_volumes(self):
        """List all EBS volumes."""
        try:
            volumes = self.resource.volumes.all()
        except botocore.exceptions.ClientError as e:
            print(e)
            return

        in_use_volumes = []
        available_volumes = []

        # Parse volumes
        for volume in volumes:
            volume_info = {
                "Volume ID": volume.id,
                "Size": f"{volume.size} GiB",
                "State": volume.state,
                "Availability Zone": volume.availability_zone
            }

            # Check if volume is attached to an instance and get mount point (device)
            mount_point = "Not Attached"
            if volume.state == "in-use":
                # Retrieve attachments and mount points
                for attachment in volume.attachments:
                    instance_id = attachment.get("InstanceId")
                    device = attachment.get("Device")
                    mount_point = f"{device} (Instance: {instance_id})"

            # Append to the appropriate list
            if volume.state == 'in-use':
                volume_info["Mount Point"] = mount_point
                in_use_volumes.append(volume_info)
            else:
                available_volumes.append(volume_info)

        # Display In-Use Volumes
        print("\nIn-Use Volumes:")
        if not in_use_volumes:
            print("No in-use volumes detected.")
        else:
            for volume in in_use_volumes:
                print(volume)

        # Display Available Volumes
        print("\nAvailable Volumes:")
        if not available_volumes:
            print("No available volumes detected.")
        else:
            for volume in available_volumes:
                print(volume)

    # COMPLETED   
    def create_volume(self):
        """Create a new EBS volume."""
        size = read_nonnegative_integer("\nEnter size (GiB) of volume to create: ")

        try:
            # Get available zones using the EC2 client
            response = self.client.describe_availability_zones()
            available_zones = [zone['ZoneName'] for zone in response['AvailabilityZones']]
            
            # Display available zones
            print("Available zones:")
            for index, zone in enumerate(available_zones, start=1):
                print(f"\t{index}. {zone}")

            # Get the zone from user input
            choice = read_range_integer("Select zone index: ", 1, len(available_zones))
            zone = available_zones[choice - 1]  # Adjust for 0-based index

            # Create the volume
            volume = self.resource.create_volume(Size=size, AvailabilityZone=zone)  # Using resource to create volume
            print(f"Created '{volume.id}'")
            
        except botocore.exceptions.ClientError as e:
            print(e)

    # COMPLETED
    def attach_volume(self):
        """Attach a volume to an EC2 instance."""
        volume_id = read_nonempty_string("\nEnter Volume ID to attach: ")
        instance_id = read_nonempty_string("Enter Instance ID to attach to: ")
        
        # List of mount points  # TODO - get dynamically
        available_devices = ['/dev/xvda', '/dev/sdf', '/dev/sdg', '/dev/sdh', '/dev/sdi', '/dev/sdj', '/dev/sdk']
        print("Available mount-points:")
        for idx, device in enumerate(available_devices, start=1):
            print(f"\t{idx}. {device}")
        
        # Get the mount point from user input
        device_index = read_range_integer("Select mount-point index: ", 1, len(available_devices))
        device = available_devices[device_index - 1]  # Adjust for 0-based index

        # Attach the volume to the instance
        try:
            volume = self.resource.Volume(volume_id)
            volume.attach_to_instance(InstanceId=instance_id, Device=device)
            print(f"Attached '{volume.id}' to '{instance_id}' at '{device}'")
        except botocore.exceptions.ClientError as e:
            print(e)

    # COMPLETED
    def detach_volume(self):
        """Detach a volume from an EC2 instance."""
        volume_id = read_nonempty_string("\nEnter Volume ID to detach: ")
        
        # Detach the volume
        try:
            volume = self.resource.Volume(volume_id)
            volume.detach_from_instance()
            print(f"Detached '{volume.id}'")
        except self.resource.meta.client.exceptions.ClientError as e:
            print(e)

    # COMPLETED
    def modify_volume(self):
        """Modify a volume's size."""
        volume_id = read_nonempty_string("\nEnter Volume ID to modify: ")
        new_size = read_nonnegative_integer("Enter new size (GiB) of volume: ")

        try:
            # Use the EC2 client to modify the volume
            self.client.modify_volume(
                VolumeId=volume_id,
                Size=new_size
            )
            print(f"Modified '{volume_id}' to {new_size} GiB")
            
        except botocore.exceptions.ClientError as e:
            print(f"Error: {e}")

    # COMPLETED
    def delete_volume(self):
        """Delete a volume."""
        volume_id = read_nonempty_string("\nEnter Volume ID to delete: ")
        
        # Delete the volume
        try:
            volume = self.resource.Volume(volume_id)
            volume.delete()
            print(f"Deleted '{volume.id}'")
        except self.resource.meta.client.exceptions.ClientError as e:
            print(e)

    # COMPLETED
    def list_snapshots(self):
        """List all snapshots."""
        snapshots = self.resource.snapshots.filter(OwnerIds=['self'])
        
        # Display snapshots
        print("\nSnapshots:")
        if not snapshots:
            print("No snapshots found.")
        else:
            for snapshot in snapshots:
                print(snapshot)
   
    # COMPLETED
    def create_snapshot(self):
        """Create a snapshot of a volume."""
        volume_id = read_nonempty_string("\nEnter available Volume ID to snapshot: ")
        description = read_nonempty_string("Enter description for snapshot: ")
        
        # Create the snapshot
        try:
            volume = self.resource.Volume(volume_id)
            snapshot = volume.create_snapshot(Description=description)
            print(f"Created '{snapshot.id}'")
        except self.resource.meta.client.exceptions.ClientError as e:
            print(e)

    # COMPLETED
    def delete_snapshot(self):
        """Delete a snapshot."""
        snapshot_id = read_nonempty_string("\nEnter Snapshot ID to delete: ")
        
        # Delete the snapshot
        try:
            snapshot = self.resource.Snapshot(snapshot_id)
            snapshot.delete()
            print(f"Deleted '{snapshot.id}'")
        except self.resource.meta.client.exceptions.ClientError as e:
            print(e)

    # COMPLETED
    def create_volume_from_snapshot(self):
        """Create a volume from a snapshot."""
        snapshot_id = read_nonempty_string("\nEnter Snapshot ID to create volume: ")

        try:
            # Get the volume ID from the snapshot
            snapshot = self.resource.Snapshot(snapshot_id)
            volume_id = snapshot.volume_id

            # Get the availability zone of the volume
            volume = self.resource.Volume(volume_id)
            availability_zone = volume.availability_zone

            # Create a new volume from the snapshot
            new_volume = self.resource.create_volume(
                SnapshotId=snapshot_id,
                AvailabilityZone=availability_zone
            )
            print(f"Created '{new_volume.id}' from '{snapshot_id}' in '{availability_zone}'")

        except Exception as e:
            print(e)
