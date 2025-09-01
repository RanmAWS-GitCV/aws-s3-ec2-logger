import boto3
from botocore.exceptions import ClientError

client = boto3.client('dynamodb', region_name = 'eu-west-2')

response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        },
    ],
    TableName='Ranmapoints_Table',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    },
    StreamSpecification={
        'StreamEnabled': False,
    },
    SSESpecification={
        'Enabled': False,
    },
    Tags=[
        {
            'Key': 'Project',
            'Value': 's3-ec2-Logger'
        },
    ],
    TableClass='STANDARD',
    DeletionProtectionEnabled=False,
)

waiter = client.get_waiter('table_exists')
waiter.wait(TableName='Ranmapoints_Table')

print("Table created successfully!")