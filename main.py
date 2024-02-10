# codded by t.me/elphad0r
"""
Every Credits dependig on this repo goes to 
Neural Programmers Offical Authors 
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
                plugins=dict(root='plugins')
                )

user_count = 0

@neural.on_message(filters.command('usercount') & filters.private)
async def user_count_command(_, message):
    await message.reply(f"Current user count: {user_count}")

@neural.on_chat_members_added()
async def count_new_users(_, message):
    global user_count
    if message.new_chat_members:
        user_count += len(message.new_chat_members)

                               
neural.run()
