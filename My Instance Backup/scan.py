import boto3
import time
import datetime
from datetime import date,timedelta
client = boto3.client('dynamodb','us-east-1')
yesterday=date.today() - timedelta(18)
formated_yesterday=yesterday.strftime('%Y-%m-%d')
epoch_yesterday=yesterday.strftime('%s')

response = client.scan(
        TableName = 'cloudtrail_events',
        IndexName = 'event_epoch_time',
        Select='ALL_ATTRIBUTES',
        Limit=123,
        KeyConditions={
            '':{
               'AttributeValueList': [
                    {
                      'N': 'event_epoch_time'
                    },
                  ],
                  'ComparisonOperator' : 'EQ'
                 }
               },
        ScanFilter={
              'Accessed_Time': {
                  'AttributeValueList':[
                      {
                        'S' : epoch_yesterday
                      },
                  ],
                  'ComparisonOperator': 'LT'
             }
                }
        )
print response
