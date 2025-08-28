import boto3

client = boto3.client('ec2', region_name='eu-west-2')

response = client.associate_iam_instance_profile(
    IamInstanceProfile={
        'Name': 'Medium-project1-logger-profile'
    },
    InstanceId='i-010539d7aa41704e4'
)