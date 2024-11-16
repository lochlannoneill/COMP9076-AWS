import datetime
from src.utils.reading_from_user import read_nonnegative_integer, read_nonempty_string, read_nonnegative_float

class CWController:
    def __init__(self, client):
        """Initialize with a boto3 session."""
        self.client = client

    # TODO
    def list_metrics(self):
        """List all CloudWatch metrics."""
        response = self.client.list_metrics()
        for metric in response['Metrics']:
            print(f"Namespace: {metric['Namespace']}")
            print(f"Metric Name: {metric['MetricName']}")
            print(f"Dimensions: {metric['Dimensions']}")
            print()

    def get_metric_statistics(self):
        # Output the average result of the given 'metric' over the last 600 seconds
        # for EC2 instance 'instance_id'

        a = self.cw.get_metric_statistics(
            Period=300,
            StartTime=datetime.datetime.utcnow() - datetime.timedelta(seconds=600),
            EndTime=datetime.datetime.utcnow(),
            MetricName=metric,
            Namespace="AWS/EC2",
            Statistics=['Average'],
            Dimensions=[{'Name':'InstanceId', 'Value':instance_id}]
            )
        print(a)

    # COMPLETED
    def set_alarm(self):
        instance_id = read_nonempty_string("Enter Instance ID to set alarm: ")
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
        print(f"Alarm created for {instance_id} if NetworkPacketsOut >= {threshold}")

    # TODO
    def delete_alarm(self):
        print("Not implemented yet.")
    
    # TODO 
    def free_tier_aws_services(self):
        print("Not implemented yet.")