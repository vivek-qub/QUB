import boto3

version_id = "s_jTXC8dofBlZ9DRMl_QrZnZtJ9XiEHE"  

session = boto3.Session(region_name='us-east-1')

s3_client = session.client('s3')

bucket_name = "qub0010127"

s3_client.download_file(
    Bucket=bucket_name,
    Key="demo/data.txt",
    Filename="data_previous_version.txt",
    ExtraArgs={'VersionId': version_id}
)


