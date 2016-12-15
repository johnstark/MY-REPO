import boto3
import datetime
eip=boto3.resource('ec2','us-east-1')
elastic=eip.filter(Filters=[{'Name':'instance','Values':['none']}])
for ip in elastic:
	print ip
