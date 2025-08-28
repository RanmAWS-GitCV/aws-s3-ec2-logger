import boto3

client = boto3.client('iam')

response = client.create_instance_profile(
    InstanceProfileName='Medium-project1-logger-profile',
    Path='/',
    Tags=[
        {
            'Key': 'Name',
    
            'Value': 'Medium-project1-logger-profile'
        },
    ]
)
