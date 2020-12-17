import os, json, boto3
from botocore.config import Config
from media_handling import swa_gifnoc
import tokens
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
from media_handling import generate_check


key_id=swa_gifnoc.read_config()

def profile_photo(msg_received,header):

    user_id = tokens.getID(header)

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    if user_id == "Error expired token" or user_id == "Error invalid token":
        return json.dumps({'Error': 'login in again'})

    else:
        cursor.execute("SELECT * FROM `profile_photo` WHERE user_id='" + str(user_id) + "';")
        row = cursor.fetchall()
        if len(row) == 1:
            for record in row:
                uniqueID=record[3]

                S3_BUCKET = "firefansapp"

                file_type = msg_received["file_type"]
                fileName="profile_photos/"+uniqueID
                my_config = Config(
                    region_name='us-west-1',

                    retries={
                        'max_attempts': 10,
                        'mode': 'standard'
                    }
                )

                s3 = boto3.client('s3', aws_access_key_id=key_id['aws_access_key_id'],
                                  aws_secret_access_key=key_id['aws_secret_access_key'], config=my_config)

                presigned_post = s3.generate_presigned_post(
                    Bucket=S3_BUCKET,
                    Key=fileName,
                    Fields={"acl": "public-read", "Content-Type": file_type},
                    Conditions=[
                        {"acl": "public-read"},
                        {"Content-Type": file_type}
                    ],
                    ExpiresIn=10800
                )
                cursor.execute("UPDATE `profile_photo` SET `profile_pic` = '" + str('https://%s.s3.amazonaws.com/%s' % (S3_BUCKET,fileName)) + "' WHERE user_id=" + str(user_id) + ";")
                conn.commit()
                conn.close()
                cursor.close()

                return json.dumps({
                    'data': presigned_post,
                    'image_url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET,fileName)
                })



def cover_photo(msg_received,header):

    user_id = tokens.getID(header)

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    if user_id == "Error expired token" or user_id == "Error invalid token":
        return json.dumps({'Error': 'login in again'})

    else:
        cursor.execute("SELECT * FROM `profile_photo` WHERE user_id='" + str(user_id) + "';")
        row = cursor.fetchall()
        if len(row) == 1:
            for record in row:
                uniqueID = record[3]

                S3_BUCKET = "firefansapp"

                file_type = msg_received["file_type"]
                fileName="cover_photos/"+uniqueID
                my_config = Config(
                    region_name='us-west-1',

                    retries={
                        'max_attempts': 10,
                        'mode': 'standard'
                    }
                )

                s3 = boto3.client('s3', aws_access_key_id=key_id['aws_access_key_id'],
                                  aws_secret_access_key=key_id['aws_secret_access_key'], config=my_config)

                presigned_post = s3.generate_presigned_post(
                    Bucket=S3_BUCKET,
                    Key=fileName,
                    Fields={"acl": "public-read", "Content-Type": file_type},
                    Conditions=[
                        {"acl": "public-read"},
                        {"Content-Type": file_type}
                    ],
                    ExpiresIn=10800
                )
                cursor.execute("UPDATE `cover_photo` SET `cover_pic` = '" + str('https://%s.s3.amazonaws.com/%s' % (S3_BUCKET,fileName)) + "' WHERE user_id=" + str(user_id) + ";")
                conn.commit()
                conn.close()
                cursor.close()

                return json.dumps({
                    'data': presigned_post,
                    'image_url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET,fileName)
                })


def post_image(msg_received,header):

    user_id = tokens.getID(header)

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    if user_id == "Error expired token" or user_id == "Error invalid token":
        return json.dumps({'Error': 'login in again'})

    else:
        cursor.execute("SELECT * FROM `user` WHERE user_id='" + str(user_id) + "';")
        row = cursor.fetchall()
        if len(row) == 1:
            for record in row:
                uniqueID = str(generate_check.wall_post_gen())

                S3_BUCKET = "firefansapp"

                file_type = msg_received["file_type"]
                fileName="post_photos/"+uniqueID+"_"+str(user_id)
                my_config = Config(
                    region_name='us-west-1',

                    retries={
                        'max_attempts': 10,
                        'mode': 'standard'
                    }
                )

                s3 = boto3.client('s3', aws_access_key_id=key_id['aws_access_key_id'],
                                  aws_secret_access_key=key_id['aws_secret_access_key'], config=my_config)

                presigned_post = s3.generate_presigned_post(
                    Bucket=S3_BUCKET,
                    Key=fileName,
                    Fields={"acl": "public-read", "Content-Type": file_type},
                    Conditions=[
                        {"acl": "public-read"},
                        {"Content-Type": file_type}
                    ],
                    ExpiresIn=10800
                )
                #cursor.execute("UPDATE `post_images` SET `image_url` = '" + str('https://%s.s3.amazonaws.com/%s' % (S3_BUCKET,fileName)) + "' AND SET `key_name` ='"+uniqueID+"' WHERE user_id=" + str(user_id) + ";")
                cursor.execute("INSERT INTO `post_images` (`id`, `user_id`, `image_url`, `date_created`, `key_name`) VALUES (NULL, '"+str(user_id)+"', '" + str('https://%s.s3.amazonaws.com/%s' % (S3_BUCKET,fileName)) + "', CURRENT_TIMESTAMP, '"+str(uniqueID)+"')")
                conn.commit()
                conn.close()
                cursor.close()

                return json.dumps({
                    'data': presigned_post,
                    'image_url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET,fileName)
                })