from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
import s3fs

def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                               key= AWS_ACCESS_KEY_ID,
                               secret = AWS_SECRET_ACCESS_KEY)
        return s3
    except Exception as e:
        print(e)

def create_bucket_if_not_exist(s3: s3fs.S3FileSystem, bucket: str):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print("Bucket created")
        else:
            print("Bucket already exists")
    except Exception as e:
        print(e)