import boto3
import time
import datetime
s3=boto3.client('s3','us-east-1')
client = boto3.client('dynamodb','us-east-1')
res=s3.list_objects(Bucket='vasanth-test-root')
reserv=s3.list_objects(Bucket='vasanth-test-log')
i=0
while(i<len(res['Contents'])):
        name = res['Contents'][i]['Key']
	print name

        time = res['Contents'][i]['LastModified']
        epoch = time.strftime('%s')
	print epoch
	print ('------------------------')
	i=i+1	
j=0
while(j<len(reserv['Contents'])):
	access = reserv['Contents'][j]['LastModified']
	epochtime = access.strftime('%s')
	print epochtime
	j=j+1
	response = client.put_item(TableName='S3_objects',Item={'Object_Name':{ 'S': name },'Last_Modified_Time':{'S': epoch },'Last_Access_Time':{'S': epochtime }})
		
		
