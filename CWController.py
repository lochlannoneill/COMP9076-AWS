import boto3
import datetime

class CWController:
    def __init__(self, session):
        """Initialize with a boto3 session."""
        self.cloudwatch = session.client('cloudwatch')

    def list_metrics(self):
        """List all CloudWatch metrics."""
        response = self.cloudwatch.list_metrics()
        for metric in response['Metrics']:
            print(f"Namespace: {metric['Namespace']}")
            print(f"Metric Name: {metric['MetricName']}")
            print(f"Dimensions: {metric['Dimensions']}")
            print()

    def get_metric_data(self):
        """Get metric data for a specified metric."""
        namespace = input("Enter the Namespace: ")
        metric_name = input("Enter the Metric Name: ")
        dimensions = input("Enter the Dimensions (comma-separated key=value): ")
        dimensions = [d.split('=') for d in dimensions.split(',')]
        start_time = input("Enter the Start Time (YYYY-MM-DD HH:MM:SS): ")
        end_time = input("Enter the End Time (YYYY-MM-DD HH:MM:SS): ")
        period = int(input("Enter the Period (in seconds): "))
        response = self.cloudwatch.get_metric_data(
            MetricDataQueries=[
                {
                    'Id': 'm1',
                    'MetricStat': {
                        'Metric': {
                            'Namespace': namespace,
                            'MetricName': metric_name,
                            'Dimensions': [{d[0]: d[1]} for d in dimensions]
                        },
                        'Period': period,
                        'Stat': 'Average'
                    },
                    'ReturnData': True
                },
            ],
            StartTime=datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S"),
            EndTime=datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        )
        print(response)

    def put_metric_data(self):
        """Put metric data for a specified metric."""
        namespace = input("Enter the Namespace: ")
        metric_name = input("Enter the Metric Name: ")
        dimensions = input("Enter the Dimensions (comma-separated key=value): ")
        dimensions = [d.split('=') for d in dimensions.split(',')]
        value = float(input("Enter the Value: "))
        timestamp = input("Enter the Timestamp (YYYY-MM-DD HH:MM:SS): ")
        response = self.cloudwatch.put_metric_data(
            Namespace=namespace,
            MetricData=[
                {
                    'MetricName': metric_name,
                    'Dimensions': [{d[0]: d[1]} for d in dimensions],
                    'Value': value,
                    'Timestamp': datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                },
            ]
        )
        print(response)