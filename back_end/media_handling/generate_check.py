from media_handling import picture_code
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import json


def generate():
    code=picture_code.generate_code()
    #print(code)
    return check(code)


def check(code):
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    #print(code)

    cursor.execute("SELECT * FROM `profile_photo` WHERE `uniqueID` ='" + str(code) + "';")
    profile_row = cursor.fetchall()
    cursor.execute("SELECT * FROM `cover_photo` WHERE `uniqueID` ='" + str(code) + "';")
    cover_row = cursor.fetchall()

    if len(profile_row) == 1 or len(cover_row) == 1:
        conn.close()
        cursor.close()
        return generate()

    else:
        conn.close()
        cursor.close()
        #print(code)
        return code

def wall_post_gen():
    return post_code(picture_code.generate_code())
#
#STRICTLY FOR IMAGES
def post_code(code):
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    # print(code)

    cursor.execute("SELECT * FROM `post_images` WHERE `key_name` ='" + str(code) + "';")
    profile_row = cursor.fetchall()
    #cursor.execute("SELECT * FROM `posts` WHERE `uniqueID` ='" + str(code) + "';")
    #cover_row = cursor.fetchall()

    if len(profile_row) == 1:
        conn.close()
        cursor.close()
        return wall_post_gen()

    else:
        conn.close()
        cursor.close()
        # print(code)
        return code


