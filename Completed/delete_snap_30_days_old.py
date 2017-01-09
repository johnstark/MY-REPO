import boto3,datetime,re
from datetime import date,timedelta

#def lambda_handler(event,context):
client=boto3.client('ec2','us-west-2')
snapshot=client.describe_snapshots(Filters=[{'Name':'owner-id','Values':['276986344560']},{'Name':'status','Values':['completed']}])
current_epoch=date.today().strftime('%s')
current=int(current_epoch)

one_month_epoch=2629743

snapshot_list = []
deleted_snap_list = []
error_list = []

for snap in snapshot['Snapshots']:
        id=snap['SnapshotId']
        #print id
        epoch=snap['StartTime'].strftime('%s')
        result=int(epoch)
        extra_epoch=result+one_month_epoch
        if extra_epoch<=current:
                snapshot_list.append(snap['SnapshotId'])
                continue
#print snapshot_list
for snap in snapshot_list:
        try:
#                client.describe_snapshots(SnapshotIds=[snap])
                client.delete_snapshot(SnapshotId=snap)
                deleted_snap_list.append(snap)
        except Exception,e:
                error_list.append(str(e))
        continue

#count number of deleted snapshots
count_a = len(deleted_snap_list)
#count number of error occured
count_error_list = len(error_list)

mystring_1 = str(deleted_snap_list)
mystring_1 = mystring_1.replace(",", "\n")

if count_error_list != 0:
        c = "\n An error occured while trying to delete the snapshot "+str(error_list)+" \n"

a = "the count of deleted snapshots are: "+str(count_a)+"\n"
b = "The deleted snapshots were :\n"+mystring_1+"\n"
output = a+b+c
#print output

#SNS to notify the result of Delete_snapshot call
sns_client = boto3.client('sns',region)
sns_response = sns_client.publish(TargetArn='arn:aws:sns:us-west-2:276986344560:VSS-DevOps-Support-Test',Message= output,Subject='Deleting Snapshots',MessageStructure='string',MessageAttributes={'string': {'DataType': 'String','StringValue': 'message',}})
