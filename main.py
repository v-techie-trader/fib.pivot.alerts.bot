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
                send_message_to_channel(msg, config.channel_1, config.tg_token_1)
                return "Sent alert", 200
            elif key == config.sec_key2:
                print(get_timestamp(), "Alert Received & Sent!")
                send_message_to_channel(msg, config.channel_2, config.tg_token_2)
                return "Sent alert", 200
            else:
                print("[X]", get_timestamp(), "Alert Received & Refused! (Wrong Key)")
                return "Refused alert", 400

    except Exception as e:
        print("[X]", get_timestamp(), "Error:\n>", e)
        logging.exception(e)
        return "Error", 400


# {
# 	"mode": "Intraday",
# 	"script": "COMPUSDTPERP",
# 	"close": 10.2,
# 	"trade_type": "SHORT",
# 	"rsi_trading_timeframe": 37,
# 	"rsi_higher_timeframe": 30,
# 	"trading_timeframe": "15",
# 	"higher_timeframe": "D",
# 	"avg": 12.20,
# 	"entry": 11.2,
# 	"t1": 11,
# 	"t2": 10.9,
# 	"avg_level": "R3",
# 	"entry_level": "R2",
# 	"t1_level": "R1",
# 	"t2_level": "P "
# }

@app.route("/<name>/alerts", methods=["POST"])
def valerts(name):
   try:
        if request.method == "POST":
            msg = str(request.get_data(as_text=True))
            key = name
            
            logging.info(f"--- data '{key}' ") # data-> {msg} \n")
            json_data=json.loads(msg)
            mode = json_data['mode']
            script = json_data['script']
            close = json_data['close']
            trade_type = json_data['trade_type']
            rsi_trading_timeframe = json_data['rsi_trading_timeframe']
            rsi_higher_timeframe= json_data['rsi_higher_timeframe']
            trading_timeframe = json_data['trading_timeframe']
            higher_timeframe=json_data['higher_timeframe']
            avg = json_data['avg']
            entry=json_data['entry']
            t1= json_data['t1']
            t2=json_data['t2']
            avg_level = json_data['avg_level']
            entry_level=json_data['entry_level']
            t1_level= json_data['t1_level']
            t2_level=json_data['t2_level']
            chart_link=json_data['chart_link']


            message = f"<u>{mode} <b>{trade_type} {script}</b> @ {entry_level}</u>\n"
            message += f"<a href=\"{chart_link}\">Chart in Tradingview</a>\n\n"
            if(trade_type=="SHORT"):
                message+=\
                f"<pre>|- {avg_level}   AVG      {avg}</pre>\n" + \
                f"<pre>|- {entry_level}   [ENTRY]  {entry}</pre>\n" +\
                f"<pre>|- {t1_level}   T1       {t1}</pre>\n" +\
                f"<pre>|- {t2_level}   T2       {t2}</pre>\n\n"

            elif (trade_type=="LONG"):
                message+=\
                f"<pre>|- {t2_level}   T2       {t2}</pre>\n" +\
                f"<pre>|- {t1_level}   T1       {t1}</pre>\n" +\
                f"<pre>|- {entry_level}   [ENTRY]  {entry}</pre>\n" +\
                f"<pre>|- {avg_level}   AVG      {avg}</pre>\n\n" 
           
            message +=f"<b><u>CMP</u></b> : <i>{close}</i>    <b><u>RSI {trading_timeframe}</u></b> : <i>{rsi_trading_timeframe}</i>      <b><u>RSI  {higher_timeframe}</u></b> : <i>{rsi_higher_timeframe}</i>\n"
    
            logging.info(f"\n{message}")
            if key == config.sec_key1:
                print(get_timestamp(), "Alert Received & Sent!")
                send_message_to_channel(message, config.channel_1, config.tg_token_1)
                return "Sent alert", 200
            elif key == config.sec_key2:
                print(get_timestamp(), "Alert Received & Sent!")
                send_message_to_channel(message, config.channel_2, config.tg_token_2)
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
    return "v.alerts.bot Running" , 200

if __name__ == "__main__":
    app.run()