import boto3

client = boto3.client('ec2','us-east-1')

response = client.describe_instances()

print response

