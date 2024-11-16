import botocore
from tabulate import tabulate
from src.utils.reading_from_user import read_nonnegative_integer, read_nonempty_string

class EBSController:
    def __init__(self, resource):
        """Initialize with a boto3 resource for EC2."""
        self.resource = resource

    def list_volumes(self):
        """List all EBS volumes."""
        try:
            volumes = self.resource.volumes.all()  # Using resource to list volumes
        except botocore.exceptions.ClientError as e:
            print(f"Error describing volumes: {e}")
            return

        in_use_volumes = []
        available_volumes = []

        # Parse volumes
        for volume in volumes:
            # Gather basic volume info
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
        try:
            available_zones = [az.name for az in self.resource.availability_zones.all()]  # Using resource for availability zones
        except botocore.exceptions.ClientError as e:
            print(f"Error retrieving availability zones: {e}")
            return
        
        print("Available zones:")
        for idx, az in enumerate(available_zones, start=1):
            print(f"\t{idx}. {az}")
        
        # Get valid availability zone from user input
        az_index = read_nonnegative_integer("Select the Availability Zone by number: ") - 1
        if 0 <= az_index < len(available_zones):
            az = available_zones[az_index]
            
            # Create the volume
            try:
                volume = self.resource.create_volume(Size=size, AvailabilityZone=az)  # Using resource to create volume
                print(f"Created '{volume.id}'")
            except botocore.exceptions.ClientError as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid zone selected.")

    def attach_volume(self):
        """Attach a volume to an EC2 instance."""
        volume_id = read_nonempty_string("\nEnter the Volume ID to attach: ")
        instance_id = read_nonempty_string("Enter the Instance ID to attach to: ")  # Ensure this is an EC2 instance ID
        
        # List of mount points  # TODO - get dynamically
        available_devices = ['/dev/xvda', '/dev/sdf', '/dev/sdg', '/dev/sdh', '/dev/sdi', '/dev/sdj', '/dev/sdk']
        
        print("Available mount points:")
        for idx, device in enumerate(available_devices, start=1):
            print(f"\t{idx}. {device}")
        
        device_index = read_nonnegative_integer("Select the mount point by number: ") - 1
        if 0 <= device_index < len(available_devices):
            device = available_devices[device_index]
            
            try:
                volume = self.resource.Volume(volume_id)  # Get the volume using resource
                volume.attach_to_instance(InstanceId=instance_id, Device=device)
                print(f"'{volume.id}' attached to '{instance_id}' at '{device}'")
            except botocore.exceptions.ClientError as e:
                print(f"Error attaching volume: {e}")
        else:
            print("Invalid device selection.")

    def detach_volume(self):
        """Detach a volume from an EC2 instance."""
        volume_id = read_nonempty_string("\nEnter the Volume ID to detach: ")
        try:
            volume = self.resource.Volume(volume_id)  # Get the volume using resource
            volume.detach_from_instance()
            print(f"'{volume.id}' detached from instance")
        except self.resource.meta.client.exceptions.ClientError as e:
            print(f"An error occurred: {e}")

    def modify_volume(self):
        """Modify a volume's size."""
        volume_id = read_nonempty_string("\nEnter the Volume ID to modify: ")
        new_size = read_nonnegative_integer("Enter the new size of the volume (GiB): ")
        try:
            volume = self.resource.Volume(volume_id)  # Get the volume using resource
            volume.modify_attribute(Size=new_size)
            print(f"Modified '{volume.id}' to {new_size} GiB")
        except self.resource.meta.client.exceptions.ClientError as e:
            print(f"An error occurred: {e}")

    def delete_volume(self):
        """Delete a volume."""
        volume_id = read_nonempty_string("\nEnter the Volume ID to delete: ")
        try:
            volume = self.resource.Volume(volume_id)  # Get the volume using resource
            volume.delete()
            print(f"Deleted '{volume.id}'")
        except self.resource.meta.client.exceptions.ClientError as e:
            print(f"An error occurred: {e}")

    def list_snapshots(self):
        """List all snapshots."""
        snapshots = self.resource.snapshots.filter(OwnerIds=['self'])  # Using resource to filter snapshots
        
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
            volume = self.resource.Volume(volume_id)  # Get the volume using resource
            snapshot = volume.create_snapshot(Description=description)
            print(f"Created '{snapshot.id}'")
        except self.resource.meta.client.exceptions.ClientError as e:
            print(f"An error occurred: {e}")

    def delete_snapshot(self):
        """Delete a snapshot."""
        snapshot_id = read_nonempty_string("\nEnter the Snapshot ID to delete: ")
        try:
            snapshot = self.resource.Snapshot(snapshot_id)  # Get the snapshot using resource
            snapshot.delete()
            print(f"Deleted '{snapshot.id}'")
        except self.resource.meta.client.exceptions.ClientError as e:
            print(f"An error occurred: {e}")

    def create_volume_from_snapshot(self):
        """Create a volume from a snapshot."""
        snapshot_id = read_nonempty_string("\nEnter the Snapshot ID to create volume from: ")

        # Optionally, retrieve the Availability Zone by describing the snapshot's volume
        try:
            snapshot = self.resource.Snapshot(snapshot_id)  # Get snapshot using resource
            volume_id = snapshot.volume_id
            print(f"Found '{volume_id}' from '{snapshot_id}'")

            # Describe the volume to get the availability zone
            volume = self.resource.Volume(volume_id)  # Get the volume using resource
            availability_zone = volume.availability_zone
            print(f"Volume located in '{availability_zone}'")

            # Create the volume from the snapshot
            new_volume = self.resource.create_volume(
                SnapshotId=snapshot_id,
                AvailabilityZone=availability_zone
            )
            print(f"Created '{new_volume.id}' from '{snapshot_id}' in '{availability_zone}'")

        except self.resource.meta.client.exceptions.ClientError as e:
            print(f"An error occurred: {e}")
        except ValueError as e:
            print(f"ValueError: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
