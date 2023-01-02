import smtplib
from email.message import EmailMessage
import os


def email_alert(subject, body, to):
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


def txt_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = [to]
    msg["from"] = "Your Doctor"

    user = "bianiemeyer150894@gmail.com"
    PASSWORD = os.environ["PASSWORD"]
    password = PASSWORD

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


if __name__ == "__main__":
    email_alert("Bill", "Pay your bill", [
                "bia.niemeyer@hotmail.com", "bianiemeyer150894@gmail.com"])
    txt_alert("Bill", "Pay your bill", "6094716488@vtext.com")
