import boto3
import time
import datetime
from datetime import date,timedelta

client = boto3.client('iam','us-east-1')
mylist=[]
yesterday=date.today() - timedelta(30)

formated_yesterday=yesterday.strftime('%Y-%m-%d')
epoch_yesterday=yesterday.strftime('%s')
response = client.list_users(MaxItems=20)
#iprint response
#print response['Users'][0]['UserName']
#print response['Marker']
#print response['IsTruncated']
#while response['IsTruncated'] != 'False':
response = client.list_users(Marker=response['Marker'])
    #print responsee['Users'][0]['UserName']
#print responsee['IsTruncated']
for res in response['Users']['UserName']:
    #print res['UserName']
   # print username

    accesskey = client.list_access_keys(UserName = res['UserName'])
    for access in accesskey['AccessKeyMetadata']:
        time = access['CreateDate']
        #print time
        epoch = time.strftime('%s')
        #print epoch
        #if epoch < epoch_yesterday:
            #print res['UserName']

#mylist.append(accesskey)
#print accesskey['AccessKeyMetadata']
#print  type( accesskey)    

