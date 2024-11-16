import botocore
from tabulate import tabulate
from src.utils.reading_from_user import read_nonnegative_integer, read_nonempty_string, read_range_integer

class EBSController:
    def __init__(self, resource):
        """Initialize with a boto3 resource for EC2."""
        self.resource = resource

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

            # Update the volume info with mount point if it's in-use
            if volume.state == 'in-use':
                volume_info["Mount Point"] = mount_point
                in_use_volumes.append(volume_info)
            else:
                available_volumes.append(volume_info)

        # Display In-Use Volumes
        print("\nIn-Use Volumes:")
        if in_use_volumes:
            print(tabulate(in_use_volumes, headers="keys", tablefmt="pretty"))
        else:
            print("No in-use volumes detected.")

        # Display Available Volumes
        print("Available Volumes:")
        if available_volumes:
            print(tabulate(available_volumes, headers="keys", tablefmt="pretty"))
        else:
            print("No available volumes detected.")
            
    def create_volume(self):
        """Create a new EBS volume."""
        size = read_nonnegative_integer("\nEnter the size of the volume (GiB) to create: ")
        
        # Get available zones for the region dynamically
        try:
            available_zones = [az.name for az in self.resource.availability_zones.all()]
        except botocore.exceptions.ClientError as e:
            print(e)
            return
        print("Available zones:")
        for index, zone in enumerate(available_zones, start=1):
            print(f"\t{index}. {zone}")
        
        # Get valid availability zone from user input
        choice = read_range_integer("Select the Availability Zone by number: ", 1, len(available_zones))
        zone = available_zones[choice]
        
        # Create the volume
        try:
            volume = self.resource.create_volume(Size=size, AvailabilityZone=zone)  # Using resource to create volume
            print(f"Created '{volume.id}'")
        except botocore.exceptions.ClientError as e:
            print(f"An error occurred: {e}")

    def attach_volume(self):
        """Attach a volume to an EC2 instance."""
        volume_id = read_nonempty_string("\nEnter the Volume ID to attach: ")
        instance_id = read_nonempty_string("Enter the Instance ID to attach to: ")
        
        # List of mount points  # TODO - get dynamically
        available_devices = ['/dev/xvda', '/dev/sdf', '/dev/sdg', '/dev/sdh', '/dev/sdi', '/dev/sdj', '/dev/sdk']
        print("Available mount points:")
        for idx, device in enumerate(available_devices, start=1):
            print(f"\t{idx}. {device}")
        
        # Get the device index from user input
        device_index = read_range_integer("Select the mount point by number: ", 1, len(available_devices))
        device = available_devices[device_index]

        # Attach the volume
        try:
            volume = self.resource.Volume(volume_id)
            volume.attach_to_instance(InstanceId=instance_id, Device=device)
            print(f"Attached '{volume.id}' to '{instance_id}' at '{device}'")
        except botocore.exceptions.ClientError as e:
            print(e)

    def detach_volume(self):
        """Detach a volume from an EC2 instance."""
        volume_id = read_nonempty_string("\nEnter the Volume ID to detach: ")
        try:
            volume = self.resource.Volume(volume_id)
            volume.detach_from_instance()
            print(f"Detached '{volume.id}'")
        except self.resource.meta.client.exceptions.ClientError as e:
            print(e)

    def modify_volume(self):
        """Modify a volume's size."""
        volume_id = read_nonempty_string("\nEnter the Volume ID to modify: ")
        new_size = read_nonnegative_integer("Enter the new size of the volume (GiB): ")
        try:
            volume = self.resource.Volume(volume_id)  # Get the volume using resource
            volume.modify_attribute(Size=new_size)
            print(f"Modified '{volume.id}' to {new_size} GiB")
        except self.resource.meta.client.exceptions.ClientError as e:
            print(e)

    def delete_volume(self):
        """Delete a volume."""
        volume_id = read_nonempty_string("\nEnter the Volume ID to delete: ")
        try:
            volume = self.resource.Volume(volume_id)
            volume.delete()
            print(f"Deleted '{volume.id}'")
        except self.resource.meta.client.exceptions.ClientError as e:
            print(e)

    def list_snapshots(self):
        """List all snapshots."""
        snapshots = self.resource.snapshots.filter(OwnerIds=['self'])
        
        print("\nSnapshots:")
        if snapshots:
            headers = ["Snapshot ID", "Volume ID", "Size (GiB)", "Description", "Creation Date"]
            table_data = [
                [
                    snapshot.id,
                    snapshot.volume_id,
                    snapshot.volume_size,
                    snapshot.description,
                    snapshot.start_time.strftime("%Y-%m-%d %H:%M:%S")
                ]
                for snapshot in snapshots
            ]
            print(tabulate(table_data, headers=headers, tablefmt="pretty"))
        else:
            print("No snapshots found.")
   
    def create_snapshot(self):
        """Create a snapshot of a volume."""
        volume_id = read_nonempty_string("\nEnter available Volume ID to snapshot: ")
        description = read_nonempty_string("Enter a description for the snapshot: ")
        try:
            volume = self.resource.Volume(volume_id)
            snapshot = volume.create_snapshot(Description=description)
            print(f"Created '{snapshot.id}'")
        except self.resource.meta.client.exceptions.ClientError as e:
            print(e)

    def delete_snapshot(self):
        """Delete a snapshot."""
        snapshot_id = read_nonempty_string("\nEnter the Snapshot ID to delete: ")
        try:
            snapshot = self.resource.Snapshot(snapshot_id)
            snapshot.delete()
            print(f"Deleted '{snapshot.id}'")
        except self.resource.meta.client.exceptions.ClientError as e:
            print(e)

    def create_volume_from_snapshot(self):
        """Create a volume from a snapshot."""
        snapshot_id = read_nonempty_string("\nEnter the Snapshot ID to create volume from: ")

        try:
            # Get the volume ID from the snapshot
            snapshot = self.resource.Snapshot(snapshot_id)
            volume_id = snapshot.volume_id
            print(f"Found '{volume_id}' from '{snapshot_id}'")

            # Get the availability zone of the volume
            volume = self.resource.Volume(volume_id)
            availability_zone = volume.availability_zone
            print(f"Volume located in '{availability_zone}'")

            # Create a new volume from the snapshot
            new_volume = self.resource.create_volume(
                SnapshotId=snapshot_id,
                AvailabilityZone=availability_zone
            )
            print(f"Created '{new_volume.id}' from '{snapshot_id}' in '{availability_zone}'")

        except Exception as e:
            print(e)
