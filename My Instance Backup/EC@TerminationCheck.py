import boto3

#client = boto3.client('cloudtrail','us-east-1')
client = boto3.client('s3','us-east-1')

#response = client.describe_trails()
response = client.get_bucket_policy(Bucket='aws-denied-logs')


print response
#for res in response['trailList']:
    #print res['KmsKeyId']
    #print res['LogFileValidationEnabled']
 #   if 'KmsKeyId' in res:
  #      print 'Pass'
   # else:
    #    print 'Fail'


