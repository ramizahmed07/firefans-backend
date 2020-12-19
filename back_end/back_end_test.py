# importing the requests library
import requests
import json
import urllib.request
import collections
#import file as fl

# api-endpoint
#https://github.com/ramizahmed07/fb-clone.git
URL = 'http://127.0.0.1:5000'
#URL ='https://32aa993c95fd.ngrok.io'
token_home="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTAwNTQ1OTEsImlhdCI6MTYwNzQ2MjU5MSwic3ViIjoyfQ.6cDNZvyvdulh5zL6y_rVssDfF55moe4PElcxvzl5QBU"
token_google="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDk3ODQ0ODQsImlhdCI6MTYwNzE5MjQ4NCwic3ViIjo4fQ.3AqUCoAGqvnQtqwoxo_j66ID1aGmpZRB6Loud9366KQ"


def login():

    req = urllib.request.Request(URL)
    req.add_header('Content-Type', 'application/json; charset=utf-8')

    x={'subject':"login",'email':"hassanA",'password':"1234566"}
    #x = {'subject': "login", 'email': "hassan1234", 'password': "12345678"}
    body2=json.dumps(x)
    jsondata=body2.encode('utf-8')
    req.add_header('Content-Length', len(jsondata))

    r = urllib.request.urlopen(req, jsondata)
    print(r.read().decode()+"\n")


#r = requests.post(url=URL, data=jsondata,headers=header)
def register_user():
    req = urllib.request.Request(URL)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    x = {'subject': "register", 'email': "hassan.k.athumani@gmail.com", 'password': "12345678",'fullName':"Hassan",'userName':"Hassan1234",'phoneNo':" "}
    body2 = json.dumps(x)
    jsondata = body2.encode('utf-8')
    r = urllib.request.urlopen(req, jsondata)
    print(r.read().decode())

def editProf():
    req = urllib.request.Request(URL)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    req.add_header("Authorization",token_google)

    x = {
        "subject": "editProfile",
        "data": {
            "userName": "hassan",
            "fullName": "hassan",
            "subscription_price": "200",
            "bio": "wewewwew",
            "location": "Nairobi",
            "website":"www.weiwiew.com",
            "cover_photo":"www.cover.com",
            "profile_photo":"www.profile.com",
            "tags": ["", "","","",""],
            "links": {
                "facebook": "www.fb.com",
                "twitter": "www.twit.com",
                "youtube":"www.youtube.com",
                "instagram":"www.ig.com",
                "snapchat":"www.snappy.com",
                "tiktok":"www.tik.com"
            }
        }
    }
    body2 = json.dumps(x)
    jsondata = body2.encode('utf-8')
    r = urllib.request.urlopen(req, jsondata)
    print(r.read().decode())

def editMail():
    req = urllib.request.Request(URL)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    req.add_header("Authorization", token_home)

    x = {'subject': "changePass", 'password': "1234"}
    body2 = json.dumps(x)
    jsondata = body2.encode('utf-8')
    #req.add_header('Authorization', "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDk0ODkyNDUsImlhdCI6MTYwNjg5NzI0NSwic3ViIjo3MX0.09YG8f5pCvQst2EIsHYxT7ciKXU4jd5N70cruIDD1n0")

    r = urllib.request.urlopen(req, jsondata)

    print(r.read().decode())

def persist():
    req = urllib.request.Request(URL)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    req.add_header("Authorization",token_home)

    x = {'subject': "getData"}
    body2 = json.dumps(x)
    jsondata = body2.encode('utf-8')

    r = urllib.request.urlopen(req, jsondata)

    print(r.read().decode())

def change_mail():
    req = urllib.request.Request(URL)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    req.add_header("Authorization",token_home)

    x = {'subject': "changeMail","email":"johnruben150@gmail.com"}
    body2 = json.dumps(x)
    jsondata = body2.encode('utf-8')

    r = urllib.request.urlopen(req, jsondata)

    print(r.read().decode())


def upload_profile():
    req = urllib.request.Request(URL)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    req.add_header("Authorization", token_home)

    x = {'subject': "uploadProfilePhoto","file_type":"png"}
    body2 = json.dumps(x)
    jsondata = body2.encode('utf-8')

    r = urllib.request.urlopen(req, jsondata)

    print(r.read().decode())

def forgetPass():
    req = urllib.request.Request(URL)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    req.add_header("Authorization", token_home)

    x = {'subject': "forgetPass", "email": "johnruben150@gmail.com"}
    body2 = json.dumps(x)
    jsondata = body2.encode('utf-8')

    r = urllib.request.urlopen(req, jsondata)

    print(r.read().decode())

def forgetPass_code():
    req = urllib.request.Request(URL)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    req.add_header("Authorization", token_home)

    x = {'subject': "forgetPass_code", "email": "johnruben150@gmail.com","code":"rz2Xo8v7"}
    body2 = json.dumps(x)
    jsondata = body2.encode('utf-8')

    r = urllib.request.urlopen(req, jsondata)

    print(r.read().decode())

def poster():
    req = urllib.request.Request(URL)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    req.add_header("Authorization", token_home)
    x= {
        "subject": "normal_post",
        "post_details": "post_details",
        "timestamp": "timestamp"
     }
    body2 = json.dumps(x)
    jsondata = body2.encode('utf-8')

    r = urllib.request.urlopen(req, jsondata)

    print(r.read().decode())

poster()