# codded by t.me/elphad0r
"""
Every Credits depending on this repo goes to 
Neural Programmers Official Authors 
t.me/neuralp
t.me/neuralg
t.me/neuraltutor
demo bot t.me/chatgpt4vbot
   ..... t.me/askgptprobot
"""
from pyrogram import *
from config import *

neural = Client ('neural tutor',
                api_id=API_ID, 
                api_hash=API_HASH, 
                bot_token=BOT_TOKEN,
                plugins=dict(root='plugins'),
                parse_mode="html",  # Add this line for better HTML parsing
                )

# Enable debug mode and verbose logging
neural.set_parse_mode("html")
neural.log_to_console(True)
neural.log_verbosity(3)  # Set log verbosity to 3 for more detailed logging

# Start the bot
neural.run()
