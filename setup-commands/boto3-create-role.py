import boto3

client = boto3.client('iam')

response = client.create_role(
    AssumeRolePolicyDocument="""{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Principal": {
                "Service": [
                    "ec2.amazonaws.com"
                ]
            }
        }
    ]
}""",
    Path='/',
    RoleName='S3-access-for-Medium-project1-logger',
)





