# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : fabston                 #
# File Name             : handler.py              #
# ----------------------------------------------- #

import smtplib
import ssl
from email.mime.text import MIMEText
import requests


import tweepy
from discord_webhook import DiscordEmbed, DiscordWebhook
from slack_webhook import Slack
from telegram import Bot

import config

def send_message(msg):
    if config.send_telegram_alerts:
        tg_bot = Bot(token=config.tg_token_1)
        try:
            tg_bot.sendMessage(
                config.channel_1,
                msg
                .encode("latin-1", "backslashreplace")
                .decode("unicode_escape"),
                parse_mode="MARKDOWN",
            )
        except Exception as e:
            print("[X] Telegram Error:\n>", e)

def send_message_to_channel(msg, channel_, token_):
    if config.send_telegram_alerts:
        tg_bot = Bot(token=token_)
        try:
            tg_bot.sendMessage(
                channel_,
                    msg
                    .encode("latin-1", "backslashreplace")
                    .decode("unicode_escape"),
                    parse_mode="HTML",
                    disable_web_page_preview=True
            )
        except Exception as e:
            print("[X] Telegram Error:\n>", e)

def send_alert(data):
    if config.send_telegram_alerts:
        tg_bot = Bot(token=config.tg_token)
        try:
            tg_bot.sendMessage(
                data["telegram"],
                data["msg"]
                .encode("latin-1", "backslashreplace")
                .decode("unicode_escape"),
                parse_mode="MARKDOWN",
            )
        except KeyError:
            tg_bot.sendMessage(
                config.channel_1,
                data["msg"]
                .encode("latin-1", "backslashreplace")
                .decode("unicode_escape"),
                parse_mode="MARKDOWN",
            )
        except Exception as e:
            print("[X] Telegram Error:\n>", e)

    if config.send_discord_alerts:
        try:
            webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/" + data["discord"]
            )
            embed = DiscordEmbed(title=data["msg"])
            webhook.add_embed(embed)
            webhook.execute()
        except KeyError:
            webhook = DiscordWebhook(
                url="https://discord.com/api/webhooks/" + config.discord_webhook
            )
            embed = DiscordEmbed(title=data["msg"])
            webhook.add_embed(embed)
            webhook.execute()
        except Exception as e:
            print("[X] Discord Error:\n>", e)

    if config.send_slack_alerts:
        try:
            slack = Slack(url="http://127.0.0.1:8888/frostybot" + data["slack"])
            slack.post(text=data["msg"])
        except KeyError:
            slack = Slack(
                url="http://127.0.0.1:8888/frostybot" + config.slack_webhook
            )
            slack.post(text=data["msg"])
        except Exception as e:
            print("[X] Slack Error:\n>", e)
    if config.send_curl_alerts:
        try:
            headers1 = {'content-type': 'text/plain', 'Accept-Charset': 'UTF-8'}
            curl = requests.post(config.curl_webhook, data=data["msg"], headers=headers1)
            
        except Exception as e:
            print("[X] Curl Error:\n>", e)
    if config.send_twitter_alerts:
        tw_auth = tweepy.OAuthHandler(config.tw_ckey, config.tw_csecret)
        tw_auth.set_access_token(config.tw_atoken, config.tw_asecret)
        tw_api = tweepy.API(tw_auth)
        try:
            tw_api.update_status(
                status=data["msg"].replace("*", "").replace("_", "").replace("`", "")
            )
        except Exception as e:
            print("[X] Twitter Error:\n>", e)

    if config.send_email_alerts:
        try:
            email_msg = MIMEText(
                data["msg"].replace("*", "").replace("_", "").replace("`", "")
            )
            email_msg["Subject"] = config.email_subject
            email_msg["From"] = config.email_sender
            email_msg["To"] = config.email_sender
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(
                config.email_host, config.email_port, context=context
            ) as server:
                server.login(config.email_user, config.email_password)
                server.sendmail(
                    config.email_sender, config.email_receivers, email_msg.as_string()
                )
                server.quit()
        except Exception as e:
            print("[X] Email Error:\n>", e)
