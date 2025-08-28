import boto3
import json

s3 = boto3.client('s3')

bucket_name = 'ranmarket-bucket-001'  # Your bucket name here

public_read_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "PublicReadGetObject",
        "Effect": "Allow",
        "Principal": "*",
        "Action": ["s3:GetObject"],
        "Resource": [f"arn:aws:s3:::{bucket_name}/*"]
    }]
}

response = s3.put_bucket_policy(
    Bucket=bucket_name,
    Policy=json.dumps(public_read_policy)
)

print("Bucket policy set to allow public read.")
