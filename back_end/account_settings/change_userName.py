from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import collections
import json
import tokens
import pymongo
from mongoDB import mongo_config

key=mongo_config.read_config()
client = pymongo.MongoClient("mongodb://hassan:"+key['password']+"@firefans-test-shard-00-00.l9uuz.mongodb.net:27017,firefans-test-shard-00-01.l9uuz.mongodb.net:27017,firefans-test-shard-00-02.l9uuz.mongodb.net:27017/"+key['database']+"?ssl=true&replicaSet=atlas-o4g1ic-shard-0&authSource=admin&retryWrites=true&w=majority")
#db = client.test

db = client[key['database']]
collection = db["post"]

def update_userName(msg_received,header):
    userName = msg_received["userName"]
    user_id = tokens.getID(header)

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    if user_id == "Error expired token" or user_id == "Error invalid token":
        #print(header)
        conn.close()
        cursor.close()
        return json.dumps({'Error': 'login in again'})

    else:
        #print(str(user_id))

        cursor.execute("SELECT * FROM `user` WHERE user_id='" + str(user_id) + "';")
        row = cursor.fetchall()
        if len(row) == 1:
            for data in row:
                old_username=str(data[2])
                #likes
                collection.update_many({"post_likes": old_username}, {'$push': {'post_likes': str(userName) }})
                collection.update_many({"post_likes": str(userName)}, {'$pull': {'post_likes':old_username}})

                #posts
                collection.update_many({'userName': old_username}, {'$set': {'userName': str(userName)}})


                cursor.execute("UPDATE `user` SET `userName` = '" + str(userName) + "' WHERE user_id=" + str(user_id) + ";")
                conn.commit()
                conn.close()
                cursor.close()
                return json.dumps({'notification':'user name updated'})

        else:
            conn.close()
            cursor.close()
            return json.dumps({'Error':'user name not updated'})