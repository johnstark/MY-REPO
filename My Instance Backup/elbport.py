import boto3
client = boto3.client('elb','us-east-1')
response = client.describe_load_balancers()
for desc in response['LoadBalancerDescriptions']:
    for listner in desc['ListenerDescriptions']:
        for lis in listner['Listener']:
            print lis 

