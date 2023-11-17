#Amazon Cloudwatch for logging

import boto3
from datetime import datetime

cloudwatch = boto3.client('cloudwatch')
cloudwatch.put_metric_data(
    Namespace='YourNamespace',
    MetricData=[{
            'MetricName': 'YourMetric',
            'Dimensions': [{
                    'Name': 'YourDimension',
                    'Value': 'YourValue'},],
            'Timestamp': datetime.utcnow(),
            'Value': 1.0,
            'Unit': 'Count'},])

# Create a CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Put a custom metric
cloudwatch.put_metric_data(
    Namespace='YourNamespace',
    MetricData=[
        {
            'MetricName': 'YourMetric',
            'Dimensions': [
                {
                    'Name': 'YourDimension',
                    'Value': 'YourValue'
                },
            ],
            'Timestamp': datetime.utcnow(),
            'Value': 1.0,
            'Unit': 'Count'
        },
    ]
)
