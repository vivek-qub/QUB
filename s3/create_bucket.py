import boto3

qub = boto3.Session(region_name='us-east-1')
s3_client = boto3.client("s3")
bucket_name = "qub0010127"
s3_client.create_bucket(Bucket= bucket_name)