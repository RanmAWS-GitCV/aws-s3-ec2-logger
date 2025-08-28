import boto3

from datetime import datetime, timedelta, timezone

end = datetime.now(timezone.utc)
start = end - timedelta(minutes=5)


client = boto3.client('cloudwatch', region_name='eu-west-2')


response = client.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'cpuutilization',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/EC2',
                    'MetricName': 'CPUUtilization',
                    'Dimensions': [
                        {
                            'Name': 'InstanceId',
                            'Value': 'i-010539d7aa41704e4'
                        },
                    ]
                },
                'Period': 300,
                'Stat': 'Average',
            },
            'Label': 'CPU-Utilization',
            'ReturnData': True
        },
        {
            'Id': 'ebsvolumestorage',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/EC2',
                    'MetricName': 'EBSVolumeStorage',
                    'Dimensions': [
                        {
                            'Name': 'InstanceId',
                            'Value': 'i-010539d7aa41704e4'
                        },
                    ]
                },
                'Period': 300,
                'Stat': 'Average',
            },
            'Label': 'CPU-Utilization',
            'ReturnData': True
        }
    ],

    StartTime=start,
    EndTime=end,
    LabelOptions={
        'Timezone': '+0000'
    }
)
 
timestamp = end.strftime("%Y%m%d-%H%M%S")
log = f"Medium-project1-logger-log-{timestamp}"

s3_key = f'i-010539d7aa41704e4/logs/{log}.txt'
log_contents = f"Medium-project1-logger log file\nCreated at: {end}\n"
log_contents += str(response)
logs_bucket = 'aws-ec2-logs-bucket-1721a5abc6a5643798dee863f844d744d'

client = boto3.client('s3')

client.put_object(Body=log_contents, 
                  Bucket=logs_bucket, 
                  Key=s3_key
                  )