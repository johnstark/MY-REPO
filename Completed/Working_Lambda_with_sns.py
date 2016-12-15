import boto3
def lambda_handler(event, context):
	region ='us-west-2'
	#sns_client = boto3.client('sns',region)
	client = boto3.client('ec2',region)
	response = client.describe_instances(
		InstanceIds=[
			'i-0db9fb9bbe6704953','i-0040def2a34d446ca'])
	#print response
	for res in response['Reservations']:
			for ins in res['Instances']:
					#if 'IamInstanceProfile' in ins:
	#               print res
					#       for user in ins['IamInstanceProfile']:
					#               print user['Arn'][0]
					#else:
					#       print ins['InstanceId']+" dont have IAM role"
					if 'Tags' in ins:
							#for tag in ins['Tags']:
							#       save = tag
							#if save['Key'] == 'Owner' and 'Team' and 'Environment' and 'Name':
							print  ins['InstanceId']+" is Tagged"
							#else:
							#       print ins['InstanceId'] +" is not completely Tagged"
					else:
							a = ins['InstanceId'] +" is not Tagged"
							b = "InstanceType: "+ins['InstanceType']
							if 'IamInstanceProfile' in ins:
									c = ins['IamInstanceProfile']
							c = c['Arn']
							#for s in c['Arn']:
							#       print s
							d = "CreatedBy: "+str(c)
							print a
							print b
							print d
							sns_client = boto3.client('sns',region)
							sns_response = sns_client.publish(TargetArn='arn:aws:sns:us-west-2:276986344560:VSS-DevOps-Support-Test',Message= a+"\n"+b+"\n"+d,Subject='Alert on untagged-instances status',MessageStructure='string',MessageAttributes={'string': {'DataType': 'String','StringValue': 'message',}})