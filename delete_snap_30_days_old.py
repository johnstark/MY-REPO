import boto3,datetime,re
from datetime import date,timedelta

#def lambda_handler(event,context):
client=boto3.client('ec2','us-west-2')
snapshot=client.describe_snapshots(Filters=[{'Name':'owner-id','Values':['276986344560']},{'Name':'status','Values':['completed']}])
current_epoch=date.today().strftime('%s')
current=int(current_epoch)

one_month_epoch=2629743

#one_day_epoch=86400
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
		count = count + 1
		snapshot_list.append(snap['SnapshotId'])
		continue
#count = len(snapshot_list)
for snap in snapshot_list:
	try:
		#client.delete_snapshot(SnapshotId=snap)
		deleted_snap_list.append(snap)
	except Exception,e:
		error_list.append(str(e))
	continue
	
count = len(deleted_snap_list)	
print error_list+" \n"
print "the count of deleted snapshots are: "+str(count)