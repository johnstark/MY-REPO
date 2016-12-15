import boto3

client = boto3.client('ec2','us-east-1')

response = client.describe_instances()
#print response
for respect in response['Reservations']:
    res = respect['Instances'][0]['InstanceId']
    #print res
    res_ins = client.describe_instance_attribute(InstanceId=res, Attribute='disableApiTermination')
    
    if res_ins['DisableApiTermination']['Value'] == True:
        print 'pass'
    else:
        print 'Fail'
