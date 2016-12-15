import boto3

client = boto3.client('iam','us-east-1')
response = client.get_account_password_policy()
print response

a=['AllowUsersToChangePassword','RequireLowercaseCharacters','RequireUppercaseCharacters','RequireNumbers','RequireSymbols','HardExpiry','ExpirePasswords']
i=0
count = 0
#b=len(a)
#print b
for i in a:
    if response['PasswordPolicy'][i] == True:
        count+=1
if count>=3:
    print count

