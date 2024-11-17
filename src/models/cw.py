import datetime
from src.utils.reading_from_user import read_nonnegative_integer, read_nonempty_string, read_nonnegative_float

class CWController:
    def __init__(self, client, ec2_resource):
        """Initialize with a boto3 session."""
        self.client = client
        self.ec2_resource = ec2_resource

    # COMPLETED
    def get_metric_statistics(self):
            """Display the EBSReadBytes and EBSByteBalance% performance metrics for a particular EC2 instance, averaged over the last 20 minutes."""
            instance_id = read_nonempty_string("\nEnter Instance ID to get metric statistics: ")
            metrics = ['EBSReadBytes', 'EBSByteBalance%']
            minutes = 20
            end_time = datetime.datetime.utcnow()
            start_time = end_time - datetime.timedelta(minutes=minutes)

            print(f"Average metrics over {minutes} minutes for '{instance_id}':")
            try:
                for metric in metrics:
                    response = self.client.get_metric_statistics(
                        Period=300,
                        StartTime=start_time,
                        EndTime=end_time,
                        MetricName=metric,
                        Namespace="AWS/EC2",
                        Statistics=['Average'],
                        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}]
                    )

                    datapoints = response.get('Datapoints', [])
                    if not datapoints:
                        print(f"\t{metric:<24s}No data available")
                    else:
                        # Calculate the average from the data points over the 20 minutes
                        average = sum([dp['Average'] for dp in datapoints]) / len(datapoints)
                        print(f"\t{metric:<24s}{average:.2f}")
                        
            except Exception as e:
                print(f"Error getting metric statistics: {e}")

    # COMPLETED
    def set_alarm(self):
        instance_id = read_nonempty_string("\nEnter Instance ID to set alarm: ")
        alarm = read_nonempty_string("Enter alarm name: ")
        comparison_operator = 'GreaterThanOrEqualToThreshold'
        metric = 'NetworkPacketsOut'
        threshold = 1000
        region = self.client.meta.region_name
        
        try:
            # Check if the instance exists with EC2 resource
            instances = list(self.ec2_resource.instances.filter(InstanceIds=[instance_id]))
            if not instances:
                print(f"Instance '{instance_id}' does not exist.")  # TODO - not being printed, skipping to exception instead
                return
            
            self.client.put_metric_alarm(
                AlarmName=f'{alarm}',
                ComparisonOperator=comparison_operator,
                EvaluationPeriods=1,
                MetricName=metric,
                Namespace='AWS/EC2',
                Period=300,    #INSUFFICIENT_DATA error if lower than the metric period
                Statistic='Average',
                Threshold=1000,  # Trigger alarm if NetworkPacketsOut >= 1,000
                ActionsEnabled=True,
                AlarmDescription=f"Alarm to stop instance if '{metric}' {comparison_operator} {threshold}",
                Dimensions=[
                    {
                        'Name': 'InstanceId',
                        'Value': instance_id
                    },
                ],
                Unit='Count',  # Unit type for NetworkPacketsOut
                AlarmActions=[
                    f"arn:aws:automate:{region}:ec2:stop"  # Add an EC2 Stop action when the alarm triggers
                ]
            )
            print(f"Created '{alarm}' alarm for '{instance_id}' with '{metric}' using '{comparison_operator}' set to '{threshold}'")
        
        except Exception as e:
            print(e)
            
    # COMPLETED
    def delete_alarm(self):
        alarm = read_nonempty_string("Enter name of alarm to delete: ")
        
        try:
            self.client.delete_alarms(
                AlarmNames=[alarm]
            )
            print(f"Deleted '{alarm}'")
        
        except Exception as e:
            print(e)

    # TODO 
    def free_tier_aws_services(self):
        print("Not implemented yet.")