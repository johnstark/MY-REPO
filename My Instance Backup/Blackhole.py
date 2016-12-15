import boto3
client = boto3.client('ec2','us-east-1')
response = client.describe_route_tables()
#print response
#for root in response['VpcId']:
    #print root
for route in response['RouteTables']:
    #print route['RouteTableId']
    for state in route['Tags']:
        #print state
        #print state['State']
        if 'NetworkInterfaceId' and 'InstanceId' in state:
            if state['State'] == 'blackhole':
                b = state['NetworkInterfaceId']
                print b
                #print state['InstanceId']
                #print state['InstanceId']


for r in response['RouteTables']:
    #print route
    for st in r['Routes']:
        if 'VpcPeeringConnectionId' in st:
            if st['State'] == 'blackhole':
                a = st['VpcPeeringConnectionId']
            #print state['NetworkInterfaceId']
            #print state['VpcPeeringConnectionId']
            #print a[0]
        #if state['NatGatewayId'] in state:
            #print state
        #print state['Origin']
        #print state['NatGatewayId']
        #for i in state['Origin']:
            #print i['NetworkInterfaceId']
        #print state#['NetworkInterfaceId']
        #print state['GatewayId']
        #print state['State']
        #print state['DestinationCidrBlock']
        
