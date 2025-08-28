import boto3

client = boto3.client('iam')

response = client.add_role_to_instance_profile(
    InstanceProfileName='Medium-project1-logger-profile',
    RoleName='S3-access-for-Medium-project1-logger'
)

client = boto3.client('ec2', region_name='eu-west-2')

response = client.associate_iam_instance_profile(
    IamInstanceProfile={
        'Arn': 'arn:aws:iam::666091786861:instance-profile/Medium-project1-logger-profile',
        'Name': 'Medium-project1-logger-profile'
    },
    InstanceId='i-010539d7aa41704e4'
)





print(response)