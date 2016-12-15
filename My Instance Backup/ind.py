import boto3
import time
import datetime
s3=boto3.client('s3','us-east-1')
#client = boto3.client('dynamodb','us-east-1')
res=s3.list_objects(Bucket='vasanth-test-root')
print res
#i=0
while(i<len(res['Contents'])):
	name = res['Contents'][i]['Key']
	timee = res['Contents'][i]['LastModified']
	#f = str(time)
#	date_time = 'timee'
#	pattern = '%Y-%m-%d %H:%M:%S'
#	epoch = int(time.mktime(time.strptime(date_time, pattern)))
#	print epoch
	#x = time.timestamp()
	#print x
	#response = client.put_item(TableName='S3_objects',Item={'Object_Name':{ 'S': name },'Last_Modified_Time':{'S': f }})
       # current_time=datetime.datetime.now(time.tzinfo)
       # total=current_time-time
        #d = total.days
        #i=i+1
        #if d>20:
        #   print d
	

