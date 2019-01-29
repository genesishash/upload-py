import boto3
import os
import sys
import mimetypes
import shortuuid
import pathlib

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS'),
    aws_secret_access_key=os.getenv('AWS_SECRET')
)

filename = sys.argv.pop()
extension = pathlib.Path(filename).suffix
filekey = shortuuid.uuid() + extension

bucket = os.getenv('AWS_BUCKET')

s3.upload_file(filename,bucket,filekey,ExtraArgs={
    "ACL": "public-read",
    "ContentType": mimetypes.guess_type(filename)[0]
})

print(f'https://{bucket}.s3.amazonaws.com/{filekey}')

