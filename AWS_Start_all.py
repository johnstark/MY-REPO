#Importing needed packages
import boto3,urllib2,csv,time

def lambda_handler(event, context):
	#Defining region
	region ='us-west-2'

	client = boto3.client('ec2',region)

	#URL of file in the S3 bucket
	url='https://s3-us-west-2.amazonaws.com/vss-devops-support/Vasanth/Auto+Start-Stop/All.csv'
	response = urllib2.urlopen(url)
	reader = csv.reader(response)
	list_a = []
	error_list = []
	for rows in reader:
	    for row in rows:
	        try:
	            #client.describe_instances(InstanceIds=[row])
	            client.start_instances(InstanceIds=[row])
	            list_a.append(row)
	        except Exception,e:
	            error_list.append(e)
	        continue
	count = len(list_a)
	mystring = str(list_a)
	mystring = mystring.replace(",", "\n")
	c = "\n An error occured while trying to start the instance "+str(error_list)+" \n"
	b = "The count of started instances are: \n"+str(count)+" \n"
	a = "The following instances are started successfully: \n"
	output = b+a+mystring+c
	print output

	#SNS to notify the result of Delete_snapshot call
	#sns_client = boto3.client('sns',region)
	#sns_response = sns_client.publish(TargetArn='arn:aws:sns:us-west-2:276986344560:VSS-DevOps-Support-Test',Message= output,Subject='Starting instances',MessageStructure='string',MessageAttributes={'string': {'DataType': 'String','StringValue': 'message',}})