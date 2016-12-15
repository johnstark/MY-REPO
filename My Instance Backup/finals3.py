import boto3
import time
import datetime 
import re
from datetime import date,timedelta
s3=boto3.client('s3','us-east-1')
client = boto3.client('dynamodb','us-east-1')
yesterday=date.today() - timedelta(1)
formated_yesterday=yesterday.strftime('%Y-%m-%d')
epoch_yesterday=yesterday.strftime('%s')
#print epoch_yesterday
res = s3.list_objects(Bucket = 'vasanth-test-accesslog',Prefix = formated_yesterday)
#print res
for object in res.object.all():
    #key = object.key
    #print key
    body = object.get()['Body'].read()
    bb = body.split()
    print bb
    #if bb[7] == 'REST.PUT.OBJECT' or bb[7] == 'REST.GET.OBJECT':
        #response = client.update_item(TableName='S3_objects',Key={'Object_Name':{ 'S': name },'Last_Modified_Time':{'S': epoch },'Last_Access_Time':{'S': epoc
