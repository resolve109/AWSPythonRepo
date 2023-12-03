# Lambda function to check if the bucket with name lab-bucket-13443 exists
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        if bucket['Name'] == 'lab-bucket-13443':
            return True
        else:
            #create
            s3.create_bucket(Bucket='lab-bucket-13443')
            
            #upload test.txt to lab-bucket-13443
            s3.upload_file('test.txt', 'lab-bucket-13443', 'test.txt')
            
            # create a new object in lab-bucket-13443
            s3.put_object(Bucket='lab-bucket-13443', Key='test.txt', Body='Hello, World!')
            
    return False
	
	
	
	
	
	
	
	
	
	
# command to zip files addObjects.py and test.txt
# zip -r addObjects.zip addObjects.py test.txt

# aws cli command to query for iam role arn with name LambdaDeploymentRole
# aws iam get-role --role-name LambdaDeploymentRole --query 'Role.Arn' --output text

# aws cli command to upload a lambda function addObjects.zip file to the console with runtime 3.10
# aws lambda create-function --function-name addObjects --runtime python3.10 --role arn:aws:iam::283120089861:role/LambdaDeploymentRole --handler addObjects.lambda_handler --zip-file fileb://addObjects.zip


