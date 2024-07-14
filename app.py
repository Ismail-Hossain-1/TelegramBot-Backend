from flask import Flask, request
import telegram
import os, json
from dotenv import load_dotenv
load_dotenv()

bot_token=os.getenv('bot_token')
bot_user_name= os.getenv('bot_user_name')
url= os.getenv('url')

bot= telegram.Bot(token=bot_token)
TELEGRAM_URL = "https://api.telegram.org/bot{token}".format(token=bot_token)

app = Flask(__name__)
print(bot_token)
import telegram
import requests
# Config
TOKEN = os.getenv('bot_token')
TELEGRAM_URL = "https://api.telegram.org/bot{token}".format(token=TOKEN)
WEBHOOK_URL  = os.getenv('url')

# To retrieve unique user chat ID and group ID, use @IDBot
WHITELISTED_USERS = []
bot = telegram.Bot(token=TOKEN)

from typing import List, Dict, Union



app = Flask(__name__)








def sendmessage(chat_id, prompt):
    # As the bot is searchable and visble by public.
    # Limit the response of bot to only specific chat IDs.
    authorised = True if chat_id in WHITELISTED_USERS else False
                
    message = prompt
    
    

    
    

    
    
    AIchat= "You said "+ message
    
    if not authorised:
        AIchat = "You're not authorised."
    url = "{telegram_url}/sendMessage".format(telegram_url=TELEGRAM_URL)
    
    payload = {
        "text": AIchat,
        "chat_id": chat_id
        }
    
    resp = requests.get(url,params=payload)
    #print('from send Message ', resp.json())

@app.route("/", methods=["POST","GET"])
def index():
    if(request.method == "POST"):
        response = request.get_json()
        print(response)
        
       
        # To run only if 'message' exist in response.
        if 'message' in response:

            # To not response to other bots in the same group chat
            if 'entities' not in response['message']:
            
                chat_id = response["message"]["chat"]["id"]
                prompt=response["message"]["text"]
                sendmessage(chat_id, prompt)

    return "Success"

@app.route("/setwebhook/")
def setwebhook():
    s = requests.get("{telegram_url}/setWebhook?url={webhook_url}".format(telegram_url=TELEGRAM_URL,webhook_url=WEBHOOK_URL))
    print(s)
  
    if s:
        return "Success"
    else:
        return "Fail"


if __name__ == '__main__':
    app.run(debug=True, port=5001)