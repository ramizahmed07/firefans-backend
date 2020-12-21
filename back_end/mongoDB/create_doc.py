import pymongo
from pymongo import ReturnDocument
import json
from mongoDB import mongo_config
import tokens
from media_handling import picture_code
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import collections

key=mongo_config.read_config()
client = pymongo.MongoClient("mongodb://hassan:"+key['password']+"@firefans-test-shard-00-00.l9uuz.mongodb.net:27017,firefans-test-shard-00-01.l9uuz.mongodb.net:27017,firefans-test-shard-00-02.l9uuz.mongodb.net:27017/"+key['database']+"?ssl=true&replicaSet=atlas-o4g1ic-shard-0&authSource=admin&retryWrites=true&w=majority")
#db = client.test

db = client[key['database']]
collection = db["post"]

def runner():
    return check_post_code(picture_code.post_code())

def check_post_code(code):
    #checks if code is already in DB.
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `posts` WHERE post_id='" + str(code) +"';")
    row = cursor.fetchall()
    if len(row) > 0:
        conn.close()
        cursor.close()
        return runner()
    else:
        conn.close()
        cursor.close()
        return code


def add_post(msg_received,header):

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    d = collections.OrderedDict()


    user_id=tokens.getID(header)
    post_details=msg_received["post_details"]
    timestamp=msg_received["timestamps"]
    post_images=msg_received["post_images"]
    audio=msg_received["audio_files"]
    video=msg_received["video_files"]
    post_id= runner()

    images=[]

    for i in post_images:
        images.append(i)


    if user_id == "Error expired token" or user_id == "Error invalid token":
        return json.dumps({'Error': 'login in again'})

    else:
        user_post = {
            "post_id": runner(),

            "post_details": post_details,
            "posted_by": user_id,
            "timestamp": timestamp,
            "images": images,
            "post_likes": [],
            "audio":audio,
            "video":video
        }

        collection.insert_one(user_post)
        cursor.execute("INSERT INTO `posts` (`id`, `user_id`, `post_id`, `date_created`,`uniqueID`) VALUES (NULL, '" + str(user_id) + "', '" + str(post_id) + "', CURRENT_TIMESTAMP,'null');")
        conn.commit()
        conn.close()
        cursor.close()
        result=collection.find({"post_id": post_id})

        data=[]
        for i in result:
            d['post_id'] = i['post_id']
            d['post_details'] = i['post_details']
            d['posted_by'] = i['posted_by']
            d['timestamp'] = i['timestamp']
            d['images'] = i['images']
            d['audio'] = i['audio']
            d['video'] = i['video']
            d['post_likes'] = i['post_likes']

        data.append(d)

        return json.dumps(data)


def wall_post(msg_received,header):

    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    d = collections.OrderedDict()

    user_id = tokens.getID(header)
    post_details = msg_received["post_details"]
    timestamp = msg_received["timestamp"]
    #post_images = msg_received["post_images"]
    post_id= runner()
   # audio = msg_received["audio_files"]
   # video = msg_received["video_files"]


    images = []

    #for i in post_images:
     #   images.append(i)

    if user_id == "Error expired token" or user_id == "Error invalid token":
        return json.dumps({'Error': 'login in again'})

    else:
        user_post = {
            "post_id": post_id,

            "post_details": post_details,
            "posted_by": user_id,
            "timestamp": timestamp,
            "post_likes": []
        }
        #"images": images,
        #,
       #"audio": audio,
        #"video": video

        collection.insert_one(user_post)
        cursor.execute("INSERT INTO `posts` (`id`, `user_id`, `post_id`, `date_created`,`uniqueID`) VALUES (NULL, '"+str(user_id)+"', '"+str(post_id)+"', CURRENT_TIMESTAMP,'null');")
        conn.commit()
        conn.close()
        cursor.close()
        result = collection.find({"post_id": post_id})

        data=[]

        for i in result:
            d['post_id']=i['post_id']
            d['post_details']=i['post_details']
            d['posted_by']=i['posted_by']
            d['timestamp']=i['timestamp']
            d['post_likes']=i['post_likes']

        data.append(d)

        return json.dumps(data)

