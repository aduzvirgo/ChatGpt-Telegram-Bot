from pyrogram import Client as neural, filters
from helpers.buttons import *
from your_module_name import gpt  # Replace "your_module_name" with the actual module name containing the gpt function

@neural.on_message(filters.command("start"))
async def start(bot, msg):
    markup = InlineKeyboardMarkup([[channel, group], [developer, help]])
    
    # Use the gpt function to generate a response
    response = gpt("Hello")  # Replace "Hello" with the actual text you want to send to the API
    
    await msg.reply(f"**Hello {msg.from_user.first_name} I'm ChatGPT turbo 3.5 Telegram Bot powered by openai, you can ask me anything**\n\n{response}",
                    reply_markup=markup)
