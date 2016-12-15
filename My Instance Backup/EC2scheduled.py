import boto3
client = boto3.client('ec2','us-east-1')
instance_statuses = client.describe_instance_status()#Filters=[{'Name':'event.code','Values':['instance-reboot','system-reboot','system-maintenance','instance-retirement','instance-stop']}])
print instance_statuses
