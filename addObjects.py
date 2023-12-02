import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = "lab-bucket-1337"
    file_name = 'test.txt'
    file_content = 'This is a new object file.'

    # Check if the bucket exists
    response = s3.list_buckets()
    bucket_exists = any(bucket['Name'] == bucket_name for bucket in response['Buckets'])

    # If the bucket does not exist, create it
    if not bucket_exists:
        try:
            s3.create_bucket(Bucket=bucket_name)
        except Exception as e:
            print("Error creating bucket:", e)
            return False

    # Upload the file
    try:
        s3.upload_file(file_name, bucket_name, file_name)
        return True
    except Exception as e:
        print("Error uploading file:", e)
        return False


    #create a new object in lab-bucket-1337
    s3.put_object(Bucket=bucket_name, Key=file_name , Body =file_content)
