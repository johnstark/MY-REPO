import boto3
import time


def lambda_handler(event, context):
    # Enter the region your instances are in, e.g. 'us-east-1'

    region = 'us-west-2'
    
    # Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
    instances = str('i-0515532eed2872d81')
    
    # Enter your ELB here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
    
    #elb = ['VSSDevOpsautome']
    elb = 'VSSDevOpsautome'
    
    ec2 = boto3.client('ec2', region_name=region)
    elbs = boto3.client('elb', region_name=region)
    
    elbs.deregister_instances_from_load_balancer(LoadBalancerName=elb,Instances=[{'InstanceId': instances},])
    
    time.sleep(10)
    
    instances = ['i-0515532eed2872d81']
    
    ec2.stop_instances(InstanceIds=instances)
    
    print 'stopped your instances: ' + str(instances)
