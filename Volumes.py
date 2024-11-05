import boto3

class Volumes:
    def __init__(self, session):
        """Initialize with a boto3 session."""
        self.ec2 = session.client('ec2')

    def list_volumes(self):
        """List all EBS volumes."""
        response = self.ec2.describe_volumes()
        for volume in response['Volumes']:
            print(f"Volume ID: {volume['VolumeId']}")
            print(f"Size: {volume['Size']} GiB")
            print(f"State: {volume['State']}")
            print(f"Availability Zone: {volume['AvailabilityZone']}")
            print()

    def create_volume(self):
        """Create a new EBS volume."""
        size = int(input("Enter the size of the volume (GiB): "))
        az = input("Enter the Availability Zone: ")
        response = self.ec2.create_volume(Size=size, AvailabilityZone=az)
        print(f"Volume created: {response['VolumeId']}")

    def attach_volume(self):
        """Attach a volume to an EC2 instance."""
        volume_id = input("Enter the Volume ID to attach: ")
        instance_id = input("Enter the Instance ID to attach to: ")
        device = input("Enter the device name (e.g., /dev/sdf): ")
        response = self.ec2.attach_volume(VolumeId=volume_id, InstanceId=instance_id, Device=device)
        print(f"Volume attached: {response['State']}")

    def detach_volume(self):
        """Detach a volume from an EC2 instance."""
        volume_id = input("Enter the Volume ID to detach: ")
        response = self.ec2.detach_volume(VolumeId=volume_id)
        print(f"Volume detached: {response['State']}")

    def delete_volume(self):
        """Delete a volume."""
        volume_id = input("Enter the Volume ID to delete: ")
        self.ec2.delete_volume(VolumeId=volume_id)
        print(f"Deleted volume: {volume_id}")