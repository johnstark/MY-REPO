import boto3
region ='us-west-2'
client = boto3.client('ec2',region)
tag_response = client.describe_tags(Filters=[{'Name': 'resource-type','Values': ['instance' ,]},{'Name': 'key','Values': ['PowerOnHours' ,]},{'Name': 'value','Values': ['13-6' ,]},])
for res in tag_response['Tags']:
        hike = []
        hike.append(res['ResourceId'])
        for hi in range(len( hike)):
                response = client.describe_instances(InstanceIds=[hike[hi]],)
                for res in response['Reservations']:
                        for ins in res['Instances']:
                                print ins['InstanceId']
								response = client.start_instances(InstanceIds=[ins['InstanceId']],)
