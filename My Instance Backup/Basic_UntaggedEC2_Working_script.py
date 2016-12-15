import boto3

client = boto3.client('ec2','us-west-2')

response = client.describe_instances(
    InstanceIds=[
        'i-0db9fb9bbe6704953','i-0040def2a34d446ca'])
for res in response['Reservations']:
        for ins in res['Instances']:
                if 'Tags' in ins:
                        #for tag in ins['Tags']:
                        #       save = tag
                        #if save['Key'] == 'Owner' and 'Team' and 'Environment' and 'Name':
                        print  ins['InstanceId']+" is Tagged"
                        #else:
                        #       print ins['InstanceId'] +" is not completely Tagged"
                else:
                        print ins['InstanceId'] +" is not Tagged"
