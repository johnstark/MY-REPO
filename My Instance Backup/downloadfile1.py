import boto3
import time
import datetime
import re
from datetime import date,timedelta
s3 = boto3.resource('s3','us-east-1')
client = boto3.client('dynamodb','us-east-1')
yesterday=date.today() - timedelta(18)
formated_yesterday=yesterday.strftime('%Y-%m-%d')
#print yesterday
epoch_yesterday=yesterday.strftime('%s')
#print epoch_yesterday
bucket = s3.Bucket('vasanth-test-log')
for obj in bucket.objects.filter(Prefix = formated_yesterday):
    print obj
    body = obj.get()['Body'].read()
    bb=body.split()
    #print bb
    if bb[7] == 'REST.PUT.OBJECT' or bb[7] == 'REST.GET.OBJECT':
        #name1 = bb[7]
        name = bb[8]
        #print name
        #client.update_item(TableName='S3_objects',Key={'Accessed_Time':{'S': 100}})
        #client.update_item(TableName='s3_usage_details',Key={'bucket_name':'vasanth-test-bucket','object_name':name},UpdateExpression="set Accessed_Time = :a" ,ExpressionAttributeValues={':a':epoch_yesterday},ReturnValues="UPDATED_NEW")
        #Objecttype = bb[7]
        #Objectkey = bb[8]
        #print Objecttype
        #print Objectkey
        #client.update_item(TableName='s3_usage_details',Key={'bucket_name':{'S':'vasanth-test-bucket'},'object_name':{ 'S':name }},UpdateExpression="set #s = :val", ExpressionAttributeNames={"#s": "Accessed_Time"} ,ExpressionAttributeValues={':val':{"S": epoch_yesterday }})

#Client.update_item(TableName=jobStatus, Key={'job_id':{'S':jobId}, 'run_id':{'N':runId}}, UpdateExpression="set #s = :val1, end_time = :val2", ExpressionAttributeNames={"#s": "status"}, ExpressionAttributeValues={":val1": {"S": "success"}, ":val2":{"S": endTime}})
