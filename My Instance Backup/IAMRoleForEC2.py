import boto3
import json
import time
import datetime
from datetime import date,timedelta

client = boto3.client('ec2','us-east-1')
response = client.describe_instances(InstanceIds=['i-1e984a97'])
print response
for res in response['Reservations']:
    #for ins in res['Instances'][0]['NetworkInterfaces'][0]:
    #    print ins
    #print type(res['Instances'][0]['NetworkInterfaces'][0:20])
    for i in res['Instances'][0]['NetworkInterfaces']:
        print i['VpcId']

        #if 'IamInstanceProfile' in res['Instances'][0]:
         #   print res['Instances'][0]['InstanceId']
          #  print "1"
        #else:
         #   print res['Instances'][0]['InstanceId']

          #  print "0"
#print res['Instances'][0]
        #if ins['IamInstanceProfile']:
        #for name in res['InstanceId']:
            #print ins['InstanceId']
        #if 'IamInstanceProfile' in str(ins):
        #    print 'PASS'
        #else:
        #    print 'FAIL'
#ole = client.list_role_policies()
#print role

#print response

#role = iam_client.get_role(RoleName='senthil')

#print role
