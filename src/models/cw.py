import datetime
import tabulate
from src.utils.reading_from_user import read_nonnegative_integer, read_nonempty_string, read_nonnegative_float

class CWController:
    def __init__(self, client):
        """Initialize with a boto3 session."""
        self.client = client

    # COMPLETED
    def get_metric_statistics(self):
            """Display the EBSReadBytes and EBSByteBalance% performance metrics for a particular EC2 instance, averaged over the last 20 minutes."""
            instance_id = read_nonempty_string("\nEnter Instance ID to get metrics= statistics: ")
            metrics = ['EBSReadBytes', 'EBSByteBalance%']
            minutes = 20

            end_time = datetime.datetime.utcnow()
            start_time = end_time - datetime.timedelta(minutes=minutes)

            print(f"Average metrics over the last {minutes} minutes")
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
                if datapoints:
                    # Calculate the average from the data points over the 20 minutes
                    average = sum([dp['Average'] for dp in datapoints]) / len(datapoints)
                    print(f"\t{metric:<24s}{average:.2f}")
                else:
                    print(f"\t{metric:<24s}: No data available")

    # COMPLETED
    def set_alarm(self):
        instance_id = read_nonempty_string("\nEnter Instance ID to set alarm: ")
        alarm_name = read_nonempty_string("Enter alarm name: ")
        threshold = 1000
        region = self.client.meta.region_name  # Get the region from the client
        
        self.client.put_metric_alarm(
            AlarmName=f'{alarm_name}',
            ComparisonOperator='GreaterThanOrEqualToThreshold',
            EvaluationPeriods=1,
            MetricName='NetworkPacketsOut',
            Namespace='AWS/EC2',
            Period=300,    #INSUFFICIENT_DATA error if lower than the metric period
            Statistic='Average',
            Threshold=1000,  # Trigger alarm if NetworkPacketsOut >= 1,000
            ActionsEnabled=True,
            AlarmDescription=f'Alarm to stop instance if NetworkPacketsOut >= {threshold}',
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
        print(f"Alarm created for '{instance_id}' if NetworkPacketsOut >= {threshold}")

    # COMPLETED
    def delete_alarm(self):
        alarm = read_nonempty_string("Enter name of alarm to delete: ")
        
        try:
            self.client.delete_alarms(
                AlarmNames=[alarm]
            )
            print(f"Deleted '{alarm}'")
        except Exception as e:
            print(f"Error deleting alarm: {e}")

    # TODO 
    def free_tier_aws_services(self):
        print("Not implemented yet.")