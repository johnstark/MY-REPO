import boto3

client = boto3.client('iam','us-east-1')

response = client.list_users()

admin_users = 0
admin_user_names = []

for res in response['Users']:
    #print res['UserName']
    userpolicy = client.list_user_policies(UserName=res['UserName'])
    for admin in userpolicy['PolicyNames']:
        if(str(admin).lower().find('admin') != -1):
            admin_users +=1
            admin_user_names.append(str(res['UserName']))
            print admin_user_names
            if (admin_users != 2):
                print 'fail'
#print response
