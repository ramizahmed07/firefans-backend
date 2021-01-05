import pymongo
import json
from mongoDB import mongo_config
import tokens
from mysql.connector import MySQLConnection, Error ,errors
from python_mysql_dbconfig import read_db_config
from pymongo import ReturnDocument

key=mongo_config.read_config()
client = pymongo.MongoClient("mongodb://hassan:"+key['password']+"@firefans-test-shard-00-00.l9uuz.mongodb.net:27017,firefans-test-shard-00-01.l9uuz.mongodb.net:27017,firefans-test-shard-00-02.l9uuz.mongodb.net:27017/"+key['database']+"?ssl=true&replicaSet=atlas-o4g1ic-shard-0&authSource=admin&retryWrites=true&w=majority")
#db = client.test

db = client[key['database']]
collection = db["post"]

def likePost(msg_received,header):

    user_id = tokens.getID(header)
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
                userName=info[2]

               #result = collection.find({"post_id": "9r1B9RUOym" })
                result=collection.update_one({ 'post_id':post_id },{ '$push': {'post_likes':userName}})
                data=result.acknowledged

            return json.dumps({"liked":data})
        else:
            print("error occurred")

def dislikePost(msg_received,header):

    user_id = tokens.getID(header)
    post_id=msg_received["post_id"]


    if user_id == "Error expired token" or user_id == "Error invalid token":
        return json.dumps({'Error': 'login in again'})

    else:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM `user` WHERE user_id='" + str(user_id) + "';")
        account = cursor.fetchall()
        if len(account) == 1:
            data = ""
            for info in account:

                userName=info[2]

                #result = collection.delete_one({"post_id": post_id})
                result = collection.update_one({'post_id':post_id}, {'$pull': {'post_likes': userName}})
                data=result.acknowledged

            return json.dumps({"disliked":data})


