import boto3
s3=boto3.client('s3','us-east-1')
res=s3.Bucket=('vasanth-s3-project-trans2')
for obj in res.objects.filter(Prefix='/logs'):
	print(obj.key)
