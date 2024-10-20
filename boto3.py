import boto3

def list_ec2_instances(session):
    ec2 = session.client('ec2')
    # Describe all instances
    response = ec2.describe_instances()
    running_instances = []
    stopped_instances = []
    
    # Parse instances
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_info = {
                "Instance ID": instance['InstanceId'],
                "State": instance['State']['Name'],
                "Type": instance['InstanceType'],
                "Region": instance['Placement']['AvailabilityZone'],
                "Launch Time": instance['LaunchTime'].strftime("%Y-%m-%d %H:%M:%S")
            }
            if instance['State']['Name'] == 'running':
                running_instances.append(instance_info)
            else:
                stopped_instances.append(instance_info)
    
    print("\nRunning Instances:")
    for inst in running_instances:
        print(inst)
    
    print("\nStopped Instances:")
    for inst in stopped_instances:
        print(inst)

def start_ec2_instance(session):
    ec2 = session.client('ec2')
    instance_id = input("Enter the Instance ID to start: ")
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Starting instance {instance_id}...")

def stop_ec2_instance(session):
    ec2 = session.client('ec2')
    instance_id = input("Enter the Instance ID to stop: ")
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Stopping instance {instance_id}...")

def create_ami(session):
    ec2 = session.client('ec2')
    instance_id = input("Enter the Instance ID to create AMI from: ")
    ami_name = input("Enter a name for the AMI: ")
    response = ec2.create_image(InstanceId=instance_id, Name=ami_name)
    print(f"AMI created: {response['ImageId']}")

def delete_ami(session):
    ec2 = session.client('ec2')
    ami_id = input("Enter the AMI ID to delete: ")
    ec2.deregister_image(ImageId=ami_id)
    print(f"Deleted AMI: {ami_id}")
