# codded by t.me/snackshell
"""
Every Credits depending on this repo goes to 
Neural Programmers Official Authors 
t.me/neuralp
t.me/neuralg
t.me/neuraltutor
demo bot t.me/chatgpt4vbot
   ..... t.me/askgptprobot

"""
from pyrogram import Client
from config import *

neural = Client('neural tutor',
                api_id=API_ID,
                api_hash=API_HASH,
                bot_token=BOT_TOKEN,
                plugins=dict(root='plugins')
                )

neural.start()
neural.idle()
