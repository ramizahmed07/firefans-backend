from media_handling import picture_code
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

userID=" "

def user_id(id):
    generate()
    userID=id

def generate():
    code=picture_code.generate_code()
    check(code)

def check(code):
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `cover_photo` WHERE uniqueID='" + str(code) + "';")
    row = cursor.fetchall()
    if len(row) > 0:
        conn.close()
        cursor.close()
        generate()
    else:
        conn.close()
        cursor.close()
        return code