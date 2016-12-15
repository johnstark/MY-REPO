import boto3
s3 = boto3.resource('s3')
mybucket = s3.Bucket('vasanth-test-log')
for bucket in mybucket.objects.all():
    print bucket
	
