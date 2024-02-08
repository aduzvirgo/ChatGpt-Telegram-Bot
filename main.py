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
                plugins=dict(root='plugins')
                )

user_count = 0

# Command to check the user count
@neural.on_message(filters.command('users') & filters.private)
async def users_command(_, message):
    await message.reply(f"Current user count: {user_count}")

# Increment user count on new user chat
@neural.on_chat_member_updated()
async def count_new_users(_, message):
    global user_count
    if message.new_chat_members:
        user_count += len(message.new_chat_members)

# Start the bot
neural.run()
