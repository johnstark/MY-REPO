#!/usr/bin/python
import boto3
import json
import csv
import StringIO
import time
import datetime
from datetime import date,timedelta,datetime
import dateutil.parser
client = boto3.client('iam','us-east-1')
yesterday=date.today() - timedelta(30)
#print yesterday
formated_yesterday=yesterday.strftime('%Y-%m-%d')
epoch_yesterday=yesterday.strftime('%s')
response = client.generate_credential_report()
if response['State']=='COMPLETE':
    responsee = client.get_credential_report()
    hit = responsee['Content']
    f = StringIO.StringIO(hit)
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print row[4]
        #print row[7]
        print row[9]
        #if 'N/A' not in row[5] and 'password_last_changed' not in row[5] and 'not_supported' not in row[5]:
            #print row[0]
            #date_object = datetime.strptime(row[5], '%Y-%m-%dT%H:%M:%S+00:00')
            #epoch = date_object.strftime('%s')
            #print epoch 
            #if epoch < epoch_yesterday:
                #print row[0]
                #print row[1]
                #print row[2]
                #print row[3]
                #print row[4]

