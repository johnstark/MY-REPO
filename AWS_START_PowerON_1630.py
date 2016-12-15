import boto3
region ='us-west-2'
def lambda_handler(event, context):
    client = boto3.client('ec2',region)
    tag_response = client.describe_tags(Filters=[{'Name': 'resource-type','Values': ['instance' ,]},{'Name': 'key','Values': ['PowerON' ,]},{'Name': 'value','Values': ['1630' ,]},])
    for res in tag_response['Tags']:
        hike = []
        hike.append(res['ResourceId'])
        print hike
        client.start_instances(InstanceIds=hike,)