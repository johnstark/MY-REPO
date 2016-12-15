import boto3
import time
import datetime
client = boto3.client('s3')
s3 = boto3.resource('s3')
response = client.get_object(Bucket='vasanth-test-log',Key='2016-04-11-08-47-32-6CE5F66353D546A4')
print response['Body']
