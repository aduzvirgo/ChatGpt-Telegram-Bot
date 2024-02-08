from pyrogram import Client as neural
from helpers.text import *
from your_module_name import gpt  # Replace "your_module_name" with the actual module name containing the gpt function

@neural.on_callback_query()
async def calls(_, update):
    chat_id = update.message.chat.id
    call = update.data

    if call == "help":
        await update.message.reply(HELP)
    elif call == "ask_gpt":
        # Modify the following line to use your gpt function
        response = gpt("Hi")  # Replace "Hi" with the actual text you want to send to the API
        await update.message.reply(response)
    else:
        pass
