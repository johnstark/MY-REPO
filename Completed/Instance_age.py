import boto3,subprocess,urllib2,datetime
region ='us-west-2'
ec2_client = boto3.client('ec2',region)
response = ec2_client.describe_instance_attribute(InstanceId='i-0db9fb9bbe6704953',Attribute='rootDeviceName')
vol_response = ec2_client.describe_volumes(Filters=[{'Name': 'attachment.device','Values': ['/dev/xvda',]},{'Name': 'attachment.instance-id','Values': ['i-0db9fb9bbe6704953',]},],)
for vol in vol_response['Volumes']:
        for time in vol['Attachments']:
                Created_time = time['AttachTime'] #.split('(')[1].rstrip(' GMT)')
                formated_Created_time = Created_time # datetime.datetime.strptime(Created_time,'%Y-%m-%d %H:%M:%S')
#       Created_time = vol['CreateTime']
#       for Created_time in vol['CreateTime']:
#       formated_Created_time = datetime.datetime.strptime(Created_time,'%Y-%m-%d %H:%M:%S')
                current_time = datetime.datetime.now(formated_Created_time.tzinfo)
                instance_age = (current_time-formated_Created_time).days
                print instance_age
#               if ( instance_age > 30 ):
