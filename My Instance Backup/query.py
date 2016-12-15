import boto3
import time
import datetime
from datetime import date,timedelta
client = boto3.client('dynamodb','us-east-1')
yesterday=date.today() - timedelta(18)
formated_yesterday=yesterday.strftime('%Y-%m-%d')
epoch_yesterday=yesterday.strftime('%s')

response = client.query (
    TableName = 's3_usage_details',
    IndexName = 'Accessed_Time',
    Select='ALL_ATTRIBUTES',
    Limit=123,
    KeyConditions={
        'bucket_name':{
           'AttributeValueList': [
                {
                  'S': 'vasanth-test-bucket'
                },
              ],
              'ComparisonOperator' : 'EQ'
             }
           },
    QueryFilter={
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
items = response['Items']
for item in items:
    print(item['object_name'])

