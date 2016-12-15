import boto3
import time
import datetime
s3=boto3.client('s3','us-east-1')
client = boto3.client('dynamodb','us-east-1')
res=s3.list_objects(Bucket='vasanth-test-root')
print res
i=0
while(i<len(res['Contents'])):
        name = res['Contents'][i]['Key']
        time = res['Contents'][i]['LastModified']
        print name
        print time
	epoch = time.strftime('%s')
	i=i+1
        #response = client.put_item(TableName='s3_usage_details',Item={'bucket_name':{'S':'vasanth-test-bucket'},'object_name':{ 'S': name },'Created_Time':{'S': epoch },'Accessed_Time':{'S': epoch }})

