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

# Command to check the user count
@neural.on_message(filters.command('users') & filters.private)
async def users_command(_, message):
    chat_id = message.chat.id
    user_count = await neural.get_chat_members_count(chat_id)
    await message.reply(f"Current user count: {user_count}")

# Start the bot
neural.run()
