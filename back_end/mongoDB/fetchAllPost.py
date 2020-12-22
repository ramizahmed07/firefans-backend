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

def fetchAll(header):

    user_id = tokens.getID(header)


    if user_id == "Error expired token" or user_id == "Error invalid token":
        return json.dumps({'Error': 'login in again'})

    else:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM `profile_photo` WHERE user_id='" + str(user_id) + "';")
        profile_pic = cursor.fetchall()
        if len(profile_pic) == 1:
            for info in profile_pic:

                result = collection.find({"posted_by":user_id })

                data=[]

                for i in result:
                    posts={'post_id': i['post_id'],
                           'post_details': i['post_details'],
                           'userName': i['userName'],
                           'fullName':i['fullName'],
                           'posted_by':i['posted_by'],
                            'timestamp': i['timestamp'],
                            'images' : i['images'],
                           'profile_photo':info[3],
                            'audio': i['audio'],
                            'video' : i['video'],
                            'post_likes': i['post_likes']}

                    data.append(posts)

                return json.dumps(data)