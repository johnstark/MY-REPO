import boto3

client = boto3.client('ec2','us-east-1')

response = client.describe_volumes()
for res in response['Volumes']:
    if res['Encrypted'] == True:
        print 'Pass'
    else:
        print 'Fail'

