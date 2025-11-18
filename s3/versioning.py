import boto3

session = boto3.Session(region_name='us-east-1')
s3_client = session.client('s3')

bucket_name = "qub0010127"

s3_client.put_bucket_versioning(
    Bucket=bucket_name,
    VersioningConfiguration={
        'Status': 'Enabled'  
    }
)

response = s3_client.list_object_versions(Bucket=bucket_name, Prefix="demo/data.txt")

for version in response.get('Versions', []):
    print(f"VersionId: {version['VersionId']} - IsLatest: {version['IsLatest']} - LastModified: {version['LastModified']}")

