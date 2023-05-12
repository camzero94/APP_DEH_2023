from fastapi import UploadFile, HTTPException
from uuid import uuid4
import boto3
from .config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET_REGION, AWS_BUCKET_NAME



SUPPORT_FILES_TYPE = {
        'image/png':'png',
        'image/jpeg':'jpeg',
        'image/jpg':'jpg',
        }

s3 = boto3.client('s3',
                aws_access_key_id=AWS_ACCESS_KEY,
                aws_secret_access_key=AWS_SECRET_KEY,
                region_name=AWS_BUCKET_REGION
                  )


async def upload (fileImage:UploadFile):

    #Check if Image is valid
    if not fileImage:
        raise HTTPException(status_code=404, detail="Invalid File Image")

    #Check if Image size is valid
    bytesImage = await fileImage.read()
    lengthImage = len(bytesImage)
    if lengthImage > 1000000:
        raise HTTPException(status_code=404, detail="Invalid File Image Size")

    #Check if Type Image is valid
    fyle_type = fileImage.content_type
    if fyle_type not in SUPPORT_FILES_TYPE:
        raise HTTPException(status_code=404, detail="Invalid File Image Type ")

    key = f'{uuid4()}.{SUPPORT_FILES_TYPE[fyle_type]}' 

    await upload_to_s3(bytesImage, key)
    
    return key


async def upload_to_s3(file_in_bytes:bytes,key:str):
    try:
        return s3.put_object(Body=file_in_bytes, Bucket=AWS_BUCKET_NAME, Key=key)
    except Exception as e:
            print(e)


async def generate_URL(key:str):
    #If file key is null Invalid Key
    if not key:
        raise HTTPException(status_code=404, detail="Invalid Key")
    try:
        return s3.generate_presigned_url('get_object', 
                                         Params={'Bucket': AWS_BUCKET_NAME, 'Key': key}, 
                                         ExpiresIn=3600) 
    except Exception as e:
            print(e)

