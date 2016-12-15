import boto3
s3 = boto3.resource('s3')
s3.meta.client.download_file('vasanth-test-log', '2016-04-11-08-47-32-6CE5F66353D546A4', '/home/ec2-user/2016-04-11-08-47-32-6CE5F66353D546A4')
