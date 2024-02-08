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

# File to store user IDs
user_ids_file = "user_ids.txt"

# Load existing user IDs
try:
    with open(user_ids_file, "r") as file:
        user_ids = set(map(int, file.read().splitlines()))
except FileNotFoundError:
    user_ids = set()

# Command to check the user count
@neural.on_message(filters.command('users') & filters.private)
async def users_command(_, message):
    global user_ids
    user_id = message.from_user.id

    if user_id not in user_ids:
        user_ids.add(user_id)
        # Update the file with new user IDs
        with open(user_ids_file, "a") as file:
            file.write(str(user_id) + "\n")

    await message.reply(f"Current user count: {len(user_ids)}")

# Start the bot
neural.run()
