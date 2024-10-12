from passlib.context import CryptContext
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

pwd_context = CryptContext(schemes=["bcrypt"], 
                           deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, 
           hashed_password):
    return pwd_context.verify(plain_password, 
                              hashed_password)





def upload_file(bucket_name, file_name, subdirectory, object_name=None):

    s3_client = boto3.client("s3")
    bucket = "submission-storage"
    #path = "C:\\Users\\Admin\\Desktop\\HMS test file source\\test video.mp4"

    if object_name is None:
        object_name = f"{subdirectory}/{file_name}"

    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"File: {file_name}; has been successfully uploaded to bucket: {bucket_name}; in subdirectory: {subdirectory}")

    except FileNotFoundError:
        print(f'The file "{file_name}" was not found.')
    except NoCredentialsError:
        print('Credentials not available.')
    except ClientError as e:
        print(f'Error uploading file: {e}')