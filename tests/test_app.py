import boto3
from moto import mock_s3
# from mymodule import MyModel


class MyModel(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def save(self):
        s3 = boto3.client('s3', region_name='us-east-1')
        s3.put_object(Bucket='mybucket', Key=self.name, Body=self.value)

@mock_s3
def test_my_model_save():
    conn = boto3.resource('s3', region_name='us-east-1')
    # We need to create the bucket since this is all in Moto's 'virtual' AWS account
    conn.create_bucket(Bucket='mybucket')
    model_instance = MyModel('steve', 'is awesome')
    model_instance.save()
    body = conn.Object('mybucket', 'steve').get()['Body'].read().decode("utf-8")
    assert body == 'is awesome'
    print(body)
