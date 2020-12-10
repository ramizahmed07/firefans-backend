import flask
import login as me
import register,resend_verification,verify_user,editMail,edit_profile,persistance
import json
from flask_cors import CORS, cross_origin
from checkers import checkPhoneNo,checkUserName,checkEmail
from account_settings import change_email,change_password,change_phoneNo,change_userName,verify_email,isPasswordCorrect
from media_handling import upload_image
from flask import request





app = flask.Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET', 'POST'])
@cross_origin()
def chat():
    header=request.headers.get('Authorization')
    #header =request.headers['Authorization']

    msg_received = flask.request.get_json()
    msg_subject = msg_received["subject"]

    if msg_subject == "login":
        return me.getInfo(msg_received)

    elif msg_subject=="register":
        return register.register_user(msg_received)

    elif msg_subject=="check_userName":
        return checkUserName.check_userName(msg_received)


    elif msg_subject=="check_email":
        return checkEmail.check_email(msg_received)

    elif msg_subject=="check_phoneNo":
        return checkPhoneNo.check_phoneNo(msg_received)

    elif msg_subject=="resendVerification":
        return resend_verification.resendVerification(msg_received)

    elif msg_subject=="verifyUser":
        return verify_user.verify_user(msg_received)

    elif msg_subject=="editMail":
        return editMail.editMail(msg_received)

    elif msg_subject=="editProfile":
        return edit_profile.edit_profile(msg_received,header)

    elif msg_subject=="changeMail":
        return change_email.update_email(msg_received,header)

    elif msg_subject=="verifyEmail":
        return verify_email.verify_email(msg_received,header)

    elif msg_subject=="changePass":
        return change_password.update_password(msg_received,header)

    elif msg_subject == "checkPass":
        return isPasswordCorrect.update_password(msg_received,header)

    elif msg_subject=="changePhoneNo":
        return change_phoneNo.update_phoneNo(msg_received,header)

    elif msg_subject=="changeUserName":
        return change_userName.update_userName(msg_received,header)

    elif msg_subject=="uploadProfilePhoto":
        return upload_image.profile_photo(msg_received,header)

    elif msg_subject=="uploadCoverPhoto":
        return upload_image.cover_photo(msg_received,header)

    elif msg_subject=="getData":
        return persistance.persist(header)



    else:
        return json.dumps({'Error':'format not acceptable'}) #"Invalid request."


app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)


