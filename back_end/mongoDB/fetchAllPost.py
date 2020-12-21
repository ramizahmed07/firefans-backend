import pymongo
from pymongo import ReturnDocument
import json
from mongoDB import mongo_config
import tokens
import collections

key=mongo_config.read_config()
client = pymongo.MongoClient("mongodb://hassan:"+key['password']+"@firefans-test-shard-00-00.l9uuz.mongodb.net:27017,firefans-test-shard-00-01.l9uuz.mongodb.net:27017,firefans-test-shard-00-02.l9uuz.mongodb.net:27017/"+key['database']+"?ssl=true&replicaSet=atlas-o4g1ic-shard-0&authSource=admin&retryWrites=true&w=majority")
#db = client.test

db = client[key['database']]
collection = db["post"]

def fetchAll(header):


    d = collections.OrderedDict()

    user_id = tokens.getID(header)


    if user_id == "Error expired token" or user_id == "Error invalid token":
        return json.dumps({'Error': 'login in again'})

    else:

        result = collection.find({"'posted_by'":user_id })

        data=[]

        for i in result:

            data.append(i)

        return json.dumps(data)