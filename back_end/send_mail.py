import smtplib, ssl

from email.header import Header
from email.utils import formataddr
from email.mime.text import MIMEText
import email.utils
from email.utils import formatdate
import json





def sendVerification(recipient,user_name,random_number):

    port = 465

    # Create a secure SSL context
    context = ssl.create_default_context()

    msg = MIMEText('THIS IS YOUR VERIFICATION CODE '+str(random_number))

    msg['To'] = email.utils.formataddr((user_name,recipient))
    msg['From'] = email.utils.formataddr(('Firefans','noreply@firefans.co'))
    msg['Subject'] = "VERIFICATION CODE"
    msg["Date"] = formatdate(localtime=True)

    #mail_sender =formataddr((str(Header('Finance Manager', 'utf-8')),"noreply@firefans.co"))
    try:

      with smtplib.SMTP_SSL("smtp.hostinger.com", port,context=context) as server:

        #server.set_debuglevel(True)
        server.login("noreply@firefans.co", "Inferno@2020")
        server.sendmail("noreply@firefans.co",[recipient], msg.as_string())
        #print("email sent")

    except TypeError as err:
        return json.dumps({err: err.args})






