from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import *
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
import random, os
from datetime import *
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml

app = Flask(__name__)

checkin = []
for x in range(16):
    checkin.append("")

@app.route("/", methods=['GET', 'POST'])
def index():
    global checkin
    

    return render_template('index.html', checkin=checkin)

@app.route("/update", methods=['POST'])
def update():
    global checkin

    number = request.form['From']
    message = str(request.form['Body'])
    if message == "1":
        checkin[0] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "2":
        checkin[1] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "3":
        checkin[2] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "4":
        checkin[3] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "5":
        checkin[4] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "6":
        checkin[5] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "7":
        checkin[6] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "8":
        checkin[7] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "9":
        checkin[8] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "10":
        checkin[9] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "11":
        checkin[10] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "12":
        checkin[11] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "13":
        checkin[12] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "14":
        checkin[13] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "15":
        checkin[14] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "Finished":
        checkin[15] = str(datetime.now())[11:16] + "   " + str(datetime.now())[5:10]
    elif message == "Clear":
        for x in range(16):
            checkin[x]=""
    #resp_update = twiml.Response()
    #resp.update.message('Got it!')

    return message

if __name__ == "__main__":
    app.run()
