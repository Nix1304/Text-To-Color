import boto3
import pickle
from io import BytesIO

b = {1337228: {'RU': {}}}
key, bucket = 'bought.pkl', 'kurumibotpython'
s3 = boto3.resource('s3')


with BytesIO() as data:
    s3.Bucket(bucket).download_fileobj(key, data)
    data.seek(0)
    print(pickle.load(data))


data = open(key, 'rb')
print(pickle.load(data))
s3.Bucket(bucket).put_object(Key=key, Body=data)
