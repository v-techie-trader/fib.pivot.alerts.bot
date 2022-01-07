# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : fabston                 #
# File Name             : main.py                 #
# ----------------------------------------------- #

import json
import time
import logging
from flask import Flask, request

import config
from handler import *

app = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
def get_timestamp():
    timestamp = time.strftime("%Y-%m-%d %X")
    return timestamp


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        if request.method == "POST":
            data = request.get_json()
            key = data["key"]
            sleeptime = data["sleeptime"]
            sleeptime1 = int(sleeptime)
            if key == config.sec_key1:
                print(get_timestamp(), "Alert Received & Sent!")
                send_alert(data)
                return "Sent alert", 200
            elif key == config.sec_key2:
                time.sleep(sleeptime1)
                print(get_timestamp(), "Alert Received & Sent!")
                send_alert(data)
                return "Sent alert", 200
            else:
                
                print("[X]", get_timestamp(), "Alert Received & Refused! (Wrong Key)")
                return "Refused alert", 400

    except Exception as e:
        print("[X]", get_timestamp(), "Error:\n>", e)
        return "Error", 400

@app.route("/webhook1", methods=["POST"])
def webhook1():
    try:
        if request.method == "POST":
            data1 = request.get_json()
            key1 = data["key"]
            sleeptime2 = data["sleeptime"]
            sleeptime3 = int(sleeptime2)
            if key1 == config.sec_key1:
                print(get_timestamp(), "Alert Received & Sent!")
                send_alert(data)
                return "Sent alert", 200
            elif key1 == config.sec_key2:
                time.sleep(sleeptime3)
                print(get_timestamp(), "Alert Received & Sent!")
                send_alert(data)
                return "Sent alert", 200
            else:
                
                print("[X]", get_timestamp(), "Alert Received & Refused! (Wrong Key)")
                return "Refused alert", 400

    except Exception as e:
        print("[X]", get_timestamp(), "Error:\n>", e)
        return "Error", 400

@app.route("/", methods=["GET"])
def get():
    return "fib.pivot.alerts.bot Running" , 200

if __name__ == "__main__":
    from waitress import serve
    logger.info("Started")
    serve(app, host="0.0.0.0", port=8080)
