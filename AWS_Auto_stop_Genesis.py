#Importing needed packages
import boto3,urllib2,csv,time

def lambda_handler(event, context):
    #Defining region
	region ='us-west-2'

	client = boto3.client('ec2',region)

	#URL of file in the S3 bucket
	url='https://s3-us-west-2.amazonaws.com/vss-devops-support/Vasanth/Auto+Start-Stop/Genesis.csv'
	response = urllib2.urlopen(url)
	reader = csv.reader(response)
	list_a = []
	error_list = []
	for rows in reader:
	    for row in rows:
		    try:
		        #client.describe_instances(InstanceIds=[row])
		        client.stop_instances(InstanceIds=[row])
		        list_a.append(row)
		    except Exception,e:
		        error_list.append(e)
		    continue
	count = len(list_a)
	mystring = str(list_a)
	mystring = mystring.replace(",", "\n")
	c = "\n An error occured while trying to stop the instance "+str(error_list)+" \n"
	b = "The count of stopped instances are: \n"+str(count)+" \n"
	a = "The following instances are stopped successfully: \n"
	output = b+a+mystring+c
	print output

	#SNS to notify the result of Delete_snapshot call
	#sns_client = boto3.client('sns',region)
	#sns_response = sns_client.publish(TargetArn='arn:aws:sns:us-west-2:276986344560:VSS-DevOps-Support-Test',Message= output,Subject='Stopping instances',MessageStructure='string',MessageAttributes={'string': {'DataType': 'String','StringValue': 'message',}})