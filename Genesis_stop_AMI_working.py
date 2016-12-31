#Importing needed packages
import boto3,urllib2,csv,time

#Defining region
region ='us-west-2'

client = boto3.client('ec2',region)

#URL of file in the S3 bucket
url='https://s3-us-west-2.amazonaws.com/vss-devops-support/Vasanth/Auto+Start-Stop/Genesis.csv'
response = urllib2.urlopen(url)
reader = csv.reader(response)
list_a = []
list_b = []
error_list = []
for rows in reader:
        for row in rows:
                try:
                        desc_response = client.describe_instances(InstanceIds=[row])
                        for desc in desc_response['Reservations']:
                                for  ins in desc['Instances']:
                                        if ins['State']  ==  'running':
                                                #client.stop_instances(InstanceIds=[row])
                                                list_a.append(row)
                                        else:
                                                list_b.append(row)
                except Exception,e:
                        error_list.append(e)
                continue
count_a = len(list_a)
count_b = len(list_b)
count_error_list = len(error_list)


mystring_1 = str(list_a)
mystring_1 = mystring_1.replace(",", "\n")

mystring_2 = str(list_b)
mystring_2 = mystring_2.replace(",", "\n")

if count_error_list != 0:
        c = "\n An error occured while trying to stop the instance "+str(error_list)+" \n"
else:
        c = "\n There is no error while stopping the instances "
b = "The count of stopped instances are: \n"+str(count_a)+" \n"
if count_a != 0:
        a = "The following instances are stopped successfully: \n"+mystring_1
else:
        a = "All the instances are in stopped state \n"
if count_b != 0:
        d = "\n The following instances are already in stopped state: \n"+mystring_2
else:
        d = "\n All instances are in running state"
output = b+a+d+c
print output

#SNS to notify the result of Delete_snapshot call
#sns_client = boto3.client('sns',region)
#sns_response = sns_client.publish(TargetArn='arn:aws:sns:us-west-2:276986344560:VSS-DevOps-Support-Test',Message= output,Subject='Stopping instances',MessageStructure='string',MessageAttributes={'string': {'DataType': 'String','StringValue': 'message',}})
