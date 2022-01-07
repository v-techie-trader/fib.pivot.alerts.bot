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


@app.route("/<name>/webhook", methods=["POST"])
def webhook(name):
    try:
        if request.method == "POST":
            msg = str(request.get_data(as_text=True))
            key = name
            logging.info(f"--- data '{key}' {config.sec_key1} {msg}")
            if key == config.sec_key1:
                print(get_timestamp(), "Alert Received & Sent!")
                send_message(msg)
                return "Sent alert", 200
            elif key == config.sec_key2:
                print(get_timestamp(), "Alert Received & Sent!")
                send_message(msg)
                return "Sent alert", 200
            else:
                
                print("[X]", get_timestamp(), "Alert Received & Refused! (Wrong Key)")
                return "Refused alert", 400

    except Exception as e:
        print("[X]", get_timestamp(), "Error:\n>", e)
        logging.exception(e)
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
        logging.exception(e)
        return "Error", 400

@app.route("/", methods=["GET"])
def get():
    return "fib.pivot.alerts.bot Running" , 200

if __name__ == "__main__":
    app.run()