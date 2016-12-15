import boto3,urllib2,csv,time
 
#def lambda_handler(event, context):    
	region ='us-west-2'
	client = boto3.client('ec2',region)
	url = 'https://s3-us-west-2.amazonaws.com/vssprincebucket/Vasanth/InstanceName.csv'
	response = urllib2.urlopen(url)
	reader = csv.reader(response)
	for rows in reader:
			for row in rows:
					describe_response = client.describe_instances(InstanceIds=[row],)
					for des in describe_response['Reservations']:
						for ins in des['Instance']:
							ins_id = ins['InstanceId']
					client.stop_instances(InstanceIds=[row],)
					print "the instance id "+ins_id+" is stopped "
					
