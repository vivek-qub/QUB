import boto3

session = boto3.Session(region_name='us-east-1')
s3_client = session.client('s3')

bucket_name = "qub0010127"
object_name = "data.txt"  

s3_client.delete_object(Bucket=bucket_name, Key=object_name)

