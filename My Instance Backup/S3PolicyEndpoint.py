import boto3
client = boto3.client('s3')
#client = boto3.client('ec2','us-east-1')

#response = client.describe_vpc_endpoints()
res_buck = client.list_buckets()
s3_buckets = res_buck['Buckets']
for bkt in s3_buckets:
    list_bucket = bkt['Name']

response = client.get_bucket_policy(Bucket='vasanth-test-root')

print response

