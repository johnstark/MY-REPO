import boto3
import time
import datetime
from datetime import date,timedelta

client = boto3.client('iam','us-east-1')

access_list = client.list_access_keys()
for res in access_list['AccessKeyMetadata']:

    rest = res['AccessKeyId']
    #date = access_list['AccessKeyMetadata']['CreateDate']

    last_password_used = client.get_access_key_last_used(AccessKeyId=res)

    print last_password_used 
