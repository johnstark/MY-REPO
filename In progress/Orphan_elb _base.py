import boto3

region ='us-west-2'

ec2_client = boto3.client('elb',region)

response = ec2_client.describe_load_balancers() #LoadBalancerNames=['awselb-51656','awselb-19281','a$

for res in response['LoadBalancerDescriptions']:
        if res['Instances'] == []:
                print res['LoadBalancerName']