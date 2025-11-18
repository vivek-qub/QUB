import boto3

session = boto3.Session(region_name='us-east-1')
s3_client = session.client('s3')

bucket_name = "qub0010127"
file_path = "C:\\Users\\vivek\\qubryx\\data.txt"
object_name = "data.txt"

s3_client.upload_file(file_path, bucket_name, object_name)

