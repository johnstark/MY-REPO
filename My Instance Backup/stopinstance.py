import boto3
import time
# Enter the region your instances are in, e.g. 'us-east-1'

region = 'us-west-2'

# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']

instances = ['i-0515532eed2872d81']

# Enter your ELB here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']

elb = ['VSSDevOpsautome']

def lambda_handler(event, context):

    ec2 = boto3.client('ec2', region_name=region)

    ec2.start_instances(InstanceIds=instances)
	
	while True:
		print "This prints once 5 minute."
		time.sleep(300)
	
	print 'started your instances: ' + str(instances)
	
# Attach ELB	
	
	response = client.register_instances_with_load_balancer(
    LoadBalancerName=elb,
    Instances=[
        {
            'InstanceId': instances
        },
    ]
)

    