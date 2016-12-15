import boto.ec2 
conn = boto.ec2.connect_to_region("us-east-1")
addrs = conn.get_all_addresses(Filters=[{'Name':'instance_id','Values':['None']}])
for i in addrs:
   print (i.public_ip,i.instance_id)
