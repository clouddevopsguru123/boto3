import boto3

client = boto3.client('ec2',region_name='us-east-1')

response = client.run_instances(
    ImageId='ami-080e1f1',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
    KeyName='linux_practice',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'test_ec2',
                },
                {
                    'Key': 'Env',
                    'Value': 'dev',
                }
            ],
        },
    ],

)
