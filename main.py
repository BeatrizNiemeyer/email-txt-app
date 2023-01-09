#!C:\Python27\python.exe
import smtplib
from email.message import EmailMessage
import os
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


def txt_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = [to]
    msg["from"] = "Your Doctor"

    user = "bianiemeyer150894@gmail.com"
    password = "sivlwyjeuaxtdhgf"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


@app.route("/")
def home():

    return render_template("base.html")


@app.route("/info")
def info():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    verizon_phone = phone + "@vtext.com"
    subject = "Pay"
    body = f"{name}, pay your bill"
    to = f"{email}"
    print(name, phone, verizon_phone, "****************************")

    print("I AM HEEREEEEEEEEE")
    return redirect(url_for("alert", subject=subject, body=body, to=to, verizon_phone=verizon_phone))


@app.route("/<subject>/<body>/<to>/<verizon_phone>")
def alert(subject, body, to, verizon_phone):
    print("insideeeeeeee functionnnnnnnnnnn", subject, body, to)

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

    return redirect("/")


if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0", debug=True)

    # email_alert(name, "Pay your bill", email)
    # txt_alert("Bill", "Pay your bill", "6094716488@vtext.com")
