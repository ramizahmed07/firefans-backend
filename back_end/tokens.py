import jwt
import json



from mysql.connector import MySQLConnection, Error, errors
from python_mysql_dbconfig import read_db_config
from datetime import datetime, timedelta



def get_key():
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    key=" "

    try:
        cursor.execute("SELECT * FROM `random`;")
        row = cursor.fetchall()
        for record in row:
            key = record[1]
        conn.close()
        cursor.close()
        return key
    except (Error, errors) as err:
        return json.dumps({err: err.args})

def generate_token(user_id):

    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=30,seconds=0),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            get_key(),
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_token(auth_token):
    try:
        payload = jwt.decode(auth_token,get_key(), algorithm='HS256')
        return json.dumps({"notification":"valid"}) #print(str(payload['iat'])+" "+str(payload['exp']))
    except jwt.ExpiredSignatureError:
        return json.dumps({"Error":"expired"})#print('Signature expired. Please log in again.')
    except jwt.InvalidTokenError:
        return json.dumps({"Error":"invalid"}) #print('Invalid token. Please log in again.')

def getID(auth_token):
    try:
        payload = jwt.decode(auth_token, get_key(), algorithm='HS256')
        return payload['sub']  # print(str(payload['iat'])+" "+str(payload['exp']))
    except jwt.ExpiredSignatureError:
        return "Error expired token" # print('Signature expired. Please log in again.')
    except jwt.InvalidTokenError:
        return "Error invalid token"  # print('Invalid token. Please log in again.')



#p=generate_token(5)
#print(p)
#time.sleep(7)
#decode_token(p)