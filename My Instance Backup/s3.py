import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
	for object in bucket.objects.all():
		print(object.Name)
