import boto3

#specifying region

region ='us-west-2'

def lambda_handler(event, context):

    Client = boto3.Client('ec2',region)
	
	#Filtering by tag-key: PowerOffHour and tag-value: XXXX (UTC)
	
    Tag_response = client.describe_tags(Filters=[{'Name': 'resource-type','Values': ['instance' ,]},{'Name': 'key','Values': ['PowerOffHour' ,]},{'Name': 'value','Values': ['XXXX' ,]},])
	
    for resource in Tag_response['Tags']:
        tag_list = []
        tag_list.append(resource['ResourceId'])
        #API to call Start instances
        Client.stop_instances(InstanceIds=tag_list,)
