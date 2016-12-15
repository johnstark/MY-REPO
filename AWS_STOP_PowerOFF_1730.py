import boto3
region ='us-west-2'
def lambda_handler(event, context):
    client = boto3.client('ec2',region)
    tag_response = client.describe_tags(Filters=[{'Name': 'resource-type','Values': ['instance' ,]},{'Name': 'key','Values': ['PowerOFF' ,]},{'Name': 'value','Values': ['1730' ,]},])
    for res in tag_response['Tags']:
        hike = []
        hike.append(res['ResourceId'])
        client.stop_instances(InstanceIds=hike,)