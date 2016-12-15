import boto3


client = boto3.client('cloudtrail','us-east-1')

response = client.describe_trails()
 
print response
