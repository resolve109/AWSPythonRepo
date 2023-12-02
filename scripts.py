# command to zip files addObjects.py and test.txt
#zip -r addObjects.zip addObjects.py test.txt

# aws cli command to query for an iam role arn with name lambdadeplyomentrole
# aws iam get-role --role-name LambdaDeploymentRole --query 'Role.Arn' --output text

# arn:aws:iam::283120089861:role/LambdaDeploymentRole
# aws cli command to create a lambda function
# aws lambda create-function --function-name addObjects --runtime python3.8 --role arn:aws:iam::283120089861:role/LambdaDeploymentRole --handler addObjects --zip-file fileb://addObjects.zip




