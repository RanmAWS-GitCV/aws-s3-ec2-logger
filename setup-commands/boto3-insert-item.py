import boto3
from botocore.exceptions import ClientError

client = boto3.client('dynamodb', region_name = 'eu-west-2')

response = client.put_item(
    TableName='Ranmapoints_Table',
    Item={
        'id': {'N': '1'},
        'RMP': {'N': '263'}
    }
)
print(response)