import boto3,urllib2,csv
region ='us-west-2'
client = boto3.client('ec2',region)

url = 'https://s3-us-west-2.amazonaws.com/vssprincebucket/Vasanth/InstanceName.csv'
response = urllib2.urlopen(url)
reader = csv.reader(response)
for rows in reader:
        for row in rows:
                response = client.describe_instances(InstanceIds=[row],)
                print response
