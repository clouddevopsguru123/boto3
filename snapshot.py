import boto3

client = boto3.client('ec2',region_name='us-east-1')

instance = client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
        {
        'Name': 'tag:Env',
        'Values': [
            'dev'
        ]
    },
    ]
)
for instances in instance['Reservations']:
    #print(instances)
    for instanceIds in instances['Instances']:
        ids = instanceIds['InstanceId']
        print(ids)
        snap_instances = client.create_snapshots(
            InstanceSpecification={
                'InstanceId': ids
            }
        )
        #print(snap_instances['Snapshots']['SnapshotId'])
        for snap in snap_instances['Snapshots']:
            print(snap['SnapshotId'])


    
