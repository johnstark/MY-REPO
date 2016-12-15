import boto3
import time
import datetime
from datetime import date,timedelta,datetime

client = boto3.client('ec2','us-east-1')

current_date=date.today()
current_time = current_date.strftime('%s')

response = client.describe_images(
    Filters=[
        {
            'Name': 'tag:Owner',
            'Values': [
                'Pandi'
            ]
        }
    ]
)
describe_res = client.describe_instances(Filters=[
        {
            'Name': 'tag:Owner',
            'Values': [
                'Pandi'
            ]
        }
    ]
)
#for desc in describe_res['Reservations']:
#    for desc1 in desc['Instances']:
#        inst = desc1['InstanceId']
response = client.create_image(InstanceId='i-eee5ee6a',Name='UD-test-V3',NoReboot=True)
print response

for res in response['Images']:
    resi1 = res['CreationDate']
    date_object = datetime.strptime(resi1, '%Y-%m-%dT%H:%M:%S.000Z')
    sub = current_date - date_object.date()
    if (sub.days < 2):
        ami=res['ImageId']
        describe_ami = client.describe_images(ImageIds=[ami])
        for exo in res['BlockDeviceMappings']:
            snapshot_id = exo['Ebs']['SnapshotId']
            unused_ami = client.deregister_image(ImageId=ami)
            print 'ami deleted successfully are:'+ami
            response = client.delete_snapshot(SnapshotId=snapshot_id)
            print 'snapshot deleted successfully are:'+snapshot_id
        
        
