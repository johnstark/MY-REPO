import boto3
import time
import datetime
from datetime import date,timedelta,datetime
import json
import csv
import StringIO

client = boto3.client('iam','us-east-1')
mylist=[]
yesterday=date.today() - timedelta(90)

formated_yesterday=yesterday.strftime('%Y-%m-%d')
epoch_yesterday=yesterday.strftime('%s')
response1 = client.list_users()
for password in  response1['Users']:
    if 'PasswordLastUsed' in password:

        pass_time = password['PasswordLastUsed']
        passwordtime = pass_time.strftime('%s')
        print passwordtime
        accesskey = client.list_access_keys(UserName = password['UserName'])
    
        print accesskey
        if accesskey['AccessKeyMetadata']:
    
            for access in accesskey['AccessKeyMetadata']:
                time = access['CreateDate']
                #print time
                accesskeytime = time.strftime('%s')
                #print accesskeytime
                data['User'] = password
                data['Passlastused'] = pass_time
                data['Accesskeycreatedtime'] = time
                data['Account'] = account_id
                if accesskeytime < epoch_yesterday and passwordtime < epoch_yesterday:
                    data['Status'] = 'Fail'
                else:
                    data['Status'] = 'Pass'
                data['AdditionalData'] = 'N/A'
        else:
    
            data['User'] = password
            data['Passlastused'] = pass_time
            data['Accesskeycreatedtime'] = 'None'
            data['Account'] = account_id
            data['AdditionalData'] = 'No acccesskey'
            if passwordtime < epoch_yesterday:
                data['Status'] = 'Fail'
            else:
                data['Status'] = 'Pass'
            
