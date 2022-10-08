import datetime
import tempfile

import boto3


class MyModel:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def save(self):
        s3 = boto3.client('s3', region_name='us-east-1')
        s3.put_object(Bucket='mybucket', Key=self.name, Body=self.value)

    def download(self):
        s3 = boto3.client('s3', region_name='us-east-1')
        with tempfile.TemporaryFile() as fp:
            s3.download_fileobj('mybucket', self.name, fp)
