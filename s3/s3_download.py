import boto3

session = boto3.Session(region_name='us-east-1')
s3_client = session.client('s3')

bucket_name = "qub0010127"
object_key = "demo/data.txt" 
download_path = r"C:\\Users\\vivek\\Downloads\\data.txt"
s3_client.download_file(bucket_name, object_key, download_path)

with open(download_path, 'r', encoding='utf-8') as file:
    contents = file.read()
    print("File Contents:")
    print(contents)
