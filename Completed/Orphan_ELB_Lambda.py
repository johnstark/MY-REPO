#Importing package
import boto3

#Defining lambda handler
def lambda_handler(event, context):
	
	#Defining region
	region ='us-west-2'
	
	#A low-level client representing Elastic Load Balancing
	ec2_client = boto3.client('elb',region)
	
	#Creating list to collect ELB names
	OrphanELB_list = []
	
	#Describe API call 
	response = ec2_client.describe_load_balancers()
	for res in response['LoadBalancerDescriptions']:
		if res['Instances'] == []:
			OrphanELB_list.append(res['LoadBalancerName'])
			continue
	#Count number of ELBs in the list
	count = len(OrphanELB_list)
	mystring = str(OrphanELB_list)
	
	#Used to print output in new line
	mystring = mystring.replace(",", "\n")

	b = "The count of Orphan ELBs are: \n"+str(count)+" \n"
	a = "The following ELBs are orphan: \n"

	output = b+a+mystring
	print output

	#SNS to notify the result of Delete_snapshot call
	#sns_client = boto3.client('sns',region)
	#sns_response = sns_client.publish(TargetArn='arn:aws:sns:us-west-2:276986344560:VSS-DevOps-Support-Test',Message= output,Subject='Orphan ELB',MessageStructure='string',MessageAttributes={'string': {'DataType': 'String','StringValue': 'message',}})	