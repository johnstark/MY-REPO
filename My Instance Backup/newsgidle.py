import boto3
client=boto3.client('ec2','us-east-1')
response=boto3.client('elb','us-east-1')

x=0
y=0
d=0
a=[]
q=[]
l=[]
m=0

lb = response.describe_load_balancers()
for sec in lb['LoadBalancerDescriptions']:
    for u in sec['SecurityGroups']:
        d=d+1
        print u
        l.append(u)
print d
dsg=client.describe_security_groups(GroupIds=['sg-209a5c5b'])
print dsg

for s in dsg['SecurityGroups']:
        z=s['GroupId']
        x=x+1
        a.append(z)
print x
#print a
a.sort()
#print a

isg=client.describe_instances()
for v in isg['Reservations']:
        for b in v['Instances']:
                for n in b['SecurityGroups']:
                        c=n['GroupId']
                        y=y+1
                        q.append(c)
q.sort()
print q
print y
#aa=set(a)
#qq=set(q)
#print len(qq)
#print len(aa.intersection(qq))
#print [k for k in a if k not in q]
for k in a:
        if k not in q:
                #print k
                m=m+1
print m
