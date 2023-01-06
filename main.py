import smtplib
from email.message import EmailMessage
import os
from flask import Flask, request

app = Flask(__name__)


def sending_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to
    msg["from"] = "Your Doctor"

    user = "bianiemeyer150894@gmail.com"
    PASSWORD = os.environ["PASSWORD"]
    password = PASSWORD

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


@app.route('/')
def alert():

    name = request.args.get("name")
    email = request.args.get("email")
    phone = request.args.get("phone")
    account = request.args.get("account")

    subject = "Your HealthCare Facility - Action Required"
    body = f"Dear {name},\nYour account {account} has a balance pending. For more information, please access www.yourhealthcare.com to have access your balance and get more information. \nThank you"
    sending_alert(subject, body, email)
    sending_alert(subject, body, phone + "@vtext.com")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # alert("Bill", "Pay your bill", [
    #     "bia.niemeyer@hotmail.com", "bianiemeyer150894@gmail.com"])
    # alert("Bill", "Pay your bill", "6094716488@vtext.com")
