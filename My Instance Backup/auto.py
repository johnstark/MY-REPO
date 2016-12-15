import boto3
client=boto3.client('ec2','us-east-1')
response=boto3.client('elb','us-east-1')

x=0
y=0
d=0
total_sg = []
used_sg = []
m=0

lb = response.describe_load_balancers()
for sec in lb['LoadBalancerDescriptions']:
    for u in sec['SecurityGroups']:
        #d=d+1
        used_sg.append(u)

dsg=client.describe_security_groups()

for s in dsg['SecurityGroups']:
        z=s['GroupId']
        #x=x+1
        total_sg.append(z)

isg=client.describe_instances()
for v in isg['Reservations']:
        for b in v['Instances']:
                for n in b['SecurityGroups']:
                        c=n['GroupId']
                        #y=y+1
                        used_sg.append(c)

for v in dsg['SecurityGroups']:
    for h in v['IpPermissionsEgress']:
        for en in h['UserIdGroupPairs']:
            used_sg.append(en['GroupId'])
            #print used_sg

if used_sg not in total_sg:
    print total_sg


