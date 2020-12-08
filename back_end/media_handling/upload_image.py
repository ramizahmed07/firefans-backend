import os, json, boto3
from botocore.config import Config
from media_handling import swa_gifnoc as swa
from media_handling import CPgenerate_check,PPgenerate_check
import tokens
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def profile_photo(msg_received,header):

    user_id = tokens.getID(header)

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    if user_id == "Error expired token" or user_id == "Error invalid token":
        return json.dumps({'Error': 'login in again'})

    else:

        S3_BUCKET = "firefansapp"

        file_type = msg_received["file_type"]
        fileName=PPgenerate_check.user_id(user_id)
        my_config = Config(
            region_name='us-west-1',

            retries={
                'max_attempts': 10,
                'mode': 'standard'
            }
        )

        s3 = boto3.client('s3', aws_access_key_id=swa['aws_access_key_id'],
                          aws_secret_access_key=swa['aws_secret_access_key'], config=my_config)

        presigned_post = s3.generate_presigned_post(
            Bucket=S3_BUCKET,
            Key=fileName,
            Fields={"acl": "public-read", "Content-Type": file_type},
            Conditions=[
                {"acl": "public-read"},
                {"Content-Type": file_type}
            ],
            ExpiresIn=3600
        )
        cursor.execute("UPDATE `profile_photo` SET `profile_pic` = '" + str('https://%s.s3.amazonaws.com/%s' % (S3_BUCKET,"profile_photos/"+fileName)) + "' WHERE user_id=" + str(user_id) + ";")
        conn.commit()

        return json.dumps({
            'data': presigned_post,
            'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET,"profile_photos/"+fileName)
        })



def cover_photo(msg_received,header):

    user_id = tokens.getID(header)

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    if user_id == "Error expired token" or user_id == "Error invalid token":
        return json.dumps({'Error': 'login in again'})

    else:

        S3_BUCKET = "firefansapp"

        file_type = msg_received["file_type"]
        fileName=PPgenerate_check.user_id(user_id)
        my_config = Config(
            region_name='us-west-1',

            retries={
                'max_attempts': 10,
                'mode': 'standard'
            }
        )

        s3 = boto3.client('s3', aws_access_key_id=swa['aws_access_key_id'],
                          aws_secret_access_key=swa['aws_secret_access_key'], config=my_config)

        presigned_post = s3.generate_presigned_post(
            Bucket=S3_BUCKET,
            Key=fileName,
            Fields={"acl": "public-read", "Content-Type": file_type},
            Conditions=[
                {"acl": "public-read"},
                {"Content-Type": file_type}
            ],
            ExpiresIn=3600
        )
        cursor.execute("UPDATE `profile_photo` SET `cover_pic` = '" + str('https://%s.s3.amazonaws.com/%s' % (S3_BUCKET,"cover_photos/"+fileName)) + "' WHERE user_id=" + str(user_id) + ";")
        conn.commit()

        return json.dumps({
            'data': presigned_post,
            'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET,"cover_photos/"+fileName)
        })