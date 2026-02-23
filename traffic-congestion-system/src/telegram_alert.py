# telegram_alert.py
import requests

BOT_TOKEN = 'your_bot_token'
CHAT_ID = 'your_chat_id'

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=data)
    print("✅ Alert sent via Telegram")