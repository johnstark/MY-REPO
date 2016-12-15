#import common
import boto3
import StringIO
import csv
from boto3 import session
import sys
import json
#import log
import time
import datetime
from datetime import date,timedelta,datetime



client = boto3.client('iam','us-east-1')

passwordlastused = []
accesskey1lastused = []
accesskey2lastused = []

x_days=date.today() - timedelta(5)
formated_x_days=x_days.strftime('%Y-%m-%d')
epoch_x_days=x_days.strftime('%s')
credential_generate = client.generate_credential_report()
if credential_generate['State']=='COMPLETE':
    credential_get = client.get_credential_report()
    hit = credential_get['Content']
    f = StringIO.StringIO(hit)
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if 'password_enabled' not in row[3] and 'no_information' not in row[4] and '<root_account>' not in row[0]:
            if 'FALSE' not in row[3]and 'N/A'not in row[4]:
                date_object1 = datetime.strptime(row[4], '%Y-%m-%dT%H:%M:%S+00:00')
                passwordlastused = date_object1.strftime('%s')
                if 'FALSE' not in row[8]and 'N/A' not in row[10] or 'N/A' not in row[9]or 'FALSE' not in row[13] and 'N/A' not in row[15] or 'N/A' not in row[14]:
                    if 'FALSE' not in row[8]and 'N/A' not in row[10] or 'N/A' not in row[9] :
                        if 'N/A' not in row[10]:
                            date_object2 = datetime.strptime(row[10], '%Y-%m-%dT%H:%M:%S+00:00')
                            accesskey1lastused = date_object2.strftime('%s')
                        else:
                            date_object2 = datetime.strptime(row[9], '%Y-%m-%dT%H:%M:%S+00:00')
                            accesskey1lastused = date_object2.strftime('%s')
                        if 'FALSE' not in row[13] and 'N/A' not in row[15] or 'N/A' not in row[14]:
                            if 'N/A' not in row[15]:
                                date_object3 = datetime.strptime(row[15], '%Y-%m-%dT%H:%M:%S+00:00')
                                accesskey2lastused = date_object3.strftime('%s')
                            else:
                                date_object3 = datetime.strptime(row[14], '%Y-%m-%dT%H:%M:%S+00:00')
                                accesskey2lastused = date_object3.strftime('%s')                                
                            if (passwordlastused<epoch_x_days) or (accesskey1lastused<epoch_x_days) or (accesskey2lastused<epoch_x_days):
                                print "fail"
                                print row[0]
                                print row[4]
                                print row[10]
                                print row[15]
                                print row[9]
                                print row[14]
                                print 1

                            else:
                                print "PASS"
                                print row[0]
                                print row[4]
                                print row[10]
                                print row[1]
                                print row[9]
                                print row[14]
                                print 2

                    else:
                        if (passwordlastused<epoch_x_days) or (accesskey1lastused<epoch_x_days):
                            print "fail"
                            print row[0]
                            print row[4]
                            print row[10]
                            print row[15]
                            print row[9]
                            print row[14]
                            print 3
                        else:
                            print "PASS"
                            print row[0]
                            print row[4]
                            print row[10]
                            print row[15]
                            print row[9]
                            print row[14]
                            print 4

                    #if 'FALSE' not in row[13] and 'N/A' not in row[15]:
                            #date_object3 = datetime.strptime(row[15], '%Y-%m-%dT%H:%M:%S+00:00')
                            #accesskey2lastused = date_object3.strftime('%s')
                            if (passwordlastused<epoch_x_days) or (accesskey2lastused<epoch_x_days):
                                print "fail"
                                print row[0]
                                print row[4]
                                print row[10]
                                print row[15]                        
                                print row[9]
                                print row[14]

                                print 5
                            else:
                                print "PASS"
                                print row[0]
                                print row[4]
                                print row[10]
                                print row[15]                    
                                print row[9]
                                print row[14]
                                print 6
                if (passwordlastused<epoch_x_days):
                    print "fail"
                    print row[0]
                    print row[4]
                    print row[10]
                    print row[15]
                    print row[9]
                    print row[14]

                    print 7
                else:
                    print "PASS"
                    print row[0]
                    print row[4]
                    print row[10]
                    print row[15]
                    print row[9]
                    print row[14]

                    print 8

            else:
                print "false"
                print row[0]
                print row[4]
                print row[10]
                print row[15]
                print row[9]
                print row[14]
                print 9

               

