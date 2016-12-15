import boto3
client = boto3.client('ec2','us-east-1')
elb = boto3.client('elb','us-east-1')
total_sg = dict()
instance_sg = {}
grouped_sg = {}
elb_sg = {}

security_group = client.describe_security_groups()
#print security_group
for s in security_group['SecurityGroups']:
    z=s['GroupId']
    b=total_sg.append(z)
    print b
        


lb = elb.describe_load_balancers()
for sg in lb['LoadBalancerDescriptions']:
    for sec_group in sg['SecurityGroups']:
        #print sec_group
        elb_sg.append(sec_group)
        #print elb_sg


