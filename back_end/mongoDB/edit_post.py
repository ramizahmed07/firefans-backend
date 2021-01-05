import pymongo
import json
from mongoDB import mongo_config
import tokens
from mysql.connector import MySQLConnection, Error ,errors
from python_mysql_dbconfig import read_db_config

key=mongo_config.read_config()
client = pymongo.MongoClient("mongodb://hassan:"+key['password']+"@firefans-test-shard-00-00.l9uuz.mongodb.net:27017,firefans-test-shard-00-01.l9uuz.mongodb.net:27017,firefans-test-shard-00-02.l9uuz.mongodb.net:27017/"+key['database']+"?ssl=true&replicaSet=atlas-o4g1ic-shard-0&authSource=admin&retryWrites=true&w=majority")
#db = client.test

db = client[key['database']]
collection = db["post"]

def editPost(msg_received,header):

    user_id = tokens.getID(header)
    post_details=msg_received["post_details"]
    post_id=msg_received["post_id"]



    if user_id == "Error expired token" or user_id == "Error invalid token":
        return json.dumps({'Error': 'login in again'})

    else:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM user WHERE user_id='" + str(user_id) + "';")
        account = cursor.fetchall()
        if len(account) == 1:
            data=""

            for info in account:


                result=collection.update_many({'post_id': post_id}, {'$set': {'post_details': post_details}})
                data=result.acknowledged

            return json.dumps({"edited":data})
        else:
            print("error occurred")