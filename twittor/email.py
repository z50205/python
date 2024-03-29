from threading import Thread

from flask import current_app
from flask_mail import Message
from twittor import mail


def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject,recipents,text_body,html_body):
    msg=Message(
        subject=subject,recipients=recipents,reply_to='noreply@twittor.com'
    )
    msg.body=text_body
    msg.html=html_body
    Thread(target=send_async_email,args=(current_app._get_current_object(),msg)).start()