#from bson import json_util
import boto3
def lambda_handler(event, context):
	region ='us-west-2'
	ec2_client = boto3.client('elb',region)
	OrphanELB_list = []
	

	response = ec2_client.describe_load_balancers()
	for res in response['LoadBalancerDescriptions']:
		if res['Instances'] == []:
			OrphanELB_list.append(res['LoadBalancerName'])
			continue

	count = len(OrphanELB_list)
	mystring = str(OrphanELB_list)
	mystring = mystring.replace(",", "\n")

	b = "The count of Orphan ELBs are: \n"+str(count)+" \n"
	a = "The following ELBs are orphan: \n"

	output = b+a+mystring
	print output
