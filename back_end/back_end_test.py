# importing the requests library
import requests
import json
import urllib.request
import collections
#import file as fl

# api-endpoint
#https://github.com/ramizahmed07/fb-clone.git
#URL = 'http://127.0.0.1:5000'
URL ='https://32aa993c95fd.ngrok.io'
token_home="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTAwNTQ1OTEsImlhdCI6MTYwNzQ2MjU5MSwic3ViIjoyfQ.6cDNZvyvdulh5zL6y_rVssDfF55moe4PElcxvzl5QBU"
token_google="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTIzNzc3NjAsImlhdCI6MTYwOTc4NTc2MCwic3ViIjo4fQ.ZlS3sFc6_XqKE4PzzJcfsL1BVDFO2dl-R_w_5fpS7uA"


def login():

    req = urllib.request.Request(URL)
    req.add_header('Content-Type', 'application/json; charset=utf-8')

    x={'subject':"login",'email':"hassan",'password':"12345678"}
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
            "subscription_price": "500",
            "bio": "wewewwewrfhgtyjuikjjytfredswassawssddssssaawfgikklljhgfdxffddzdd",
            "location": "Nairobi",
            "website":"www.weiwiew.com",
            "cover_photo":"www.cover.com",
            "profile_photo":"www.profile.com",
            "tags": ["", "","","",""],
            "links": {
                "facebook": "www.facebook.com",
                "twitter": "www.twitter.com",
                "youtube":"www.yt.com",
                "instagram":"www.insta.com",
                "snapchat":"www.snap.com",
                "tiktok":"www.tiktok.com"
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
    req.add_header("Authorization",token_google)

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

def mega_poster():
    req = urllib.request.Request(URL)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    req.add_header("Authorization", token_google)
    x= {
        "subject":"mega_post",
            "post_details": "post_details",
            "timestamp": "timestamp",
            "images": [],
            "post_likes": [],
            "audio":[],
            "video":[]
     }
    body2 = json.dumps(x)
    jsondata = body2.encode('utf-8')

    r = urllib.request.urlopen(req, jsondata)

    print(r.read().decode())

def fetchAll():
    req = urllib.request.Request(URL)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    req.add_header("Authorization", token_google)

    x = {"subject": "fetch_all"}
    body2 = json.dumps(x)
    jsondata = body2.encode('utf-8')

    r = urllib.request.urlopen(req, jsondata)

    print(r.read().decode())

#fetchAll()
#mega_poster()
#editProf()
#change_mail()
login()