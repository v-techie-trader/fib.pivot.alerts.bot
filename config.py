# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : fabston                 #
# File Name             : config.py               #
# ----------------------------------------------- #

# TradingView Example Alert Message:
# {
# "key":"9T2q394M92", "telegram":"-1001298977502", "discord":"789842349670960670/BFeBBrCt-w2Z9RJ2wlH6TWUjM5bJuC29aJaJ5OQv9sE6zCKY_AlOxxFwRURkgEl852s3", "msg":"Long #{{ticker}} at `{{close}}`"
# }

sec_key1 = (
    "fib.pivot.alerts"  # Can be anything. Has to match with "key" in your TradingView alert message. Lenh cancel, close
)
sec_key2 = (
    "tradingview.alerts.v"  # Can be anything. Has to match with "key" in your TradingView alert message. lenh order trade
)
# Telegram Settings
send_telegram_alerts = True
tg_token_1 = "5089014574:AAGa7J9DqvM7I0Rxt7t5grxtKzF0uTwq7xE"  # Bot token. Get it from @Botfather
tg_token_2 = "5234081047:AAGzrmiBkZJk54fRvFwgBohTsxog9o0titw"  # Bot token. Get it from @Botfather
channel_1 = -1001620765727 # Channel ID (ex. -1001487568087)
channel_2 = -1001522073506 # Channel ID (ex. -1001487568087)

# Discord Settings
send_discord_alerts = False
discord_webhook = ""  # Discord Webhook URL (https://support.discordapp.com/hc/de/articles/228383668-Webhooks-verwenden)

# Slack Settings
send_slack_alerts = False
slack_webhook = ""  # Slack Webhook URL (https://api.slack.com/messaging/webhooks)

# Curl Settings
send_curl_alerts = False
curl_webhook = "http://127.0.0.1:8888/frostybot"  

# Twitter Settings
send_twitter_alerts = False
tw_ckey = ""
tw_csecret = ""
tw_atoken = ""
tw_asecret = ""

# Email Settings
send_email_alerts = False
email_sender = ""  # Your email address
email_receivers = ["", ""]  # Receivers, can be multiple
email_subject = "Trade Alert!"

email_port = 465  # SMTP SSL Port (ex. 465)
email_host = ""  # SMTP host (ex. smtp.gmail.com)
email_user = ""  # SMTP Login credentials
email_password = ""  # SMTP Login credentials
