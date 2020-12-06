import logging
from uuid import uuid4
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import json



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger()

PORT = int(os.environ.get('PORT','8443'))
URL = "https://webhooksbots.herokuapp.com/"
TOKEN ="1414314993:AAG-3ybEHFIH52KgfFsR0IpcuDF65YZ3JkA"

def start(update, context):
   
    update.message.reply_text('Hola como estas?')


def help_command(update, context):
    
    update.message.reply_text('Help!')



def put(update, context):

    texto=str(update)

    update.message.reply_text(texto)



def main():
    """Start the bot."""

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

   #Aqui configuras los comandos
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler('put', put))

    updater.start_webhook(listen = "0.0.0.0",port=PORT,url_path=TOKEN)

    updater.start_webhook(URL+TOKEN)
    


    updater.idle()


if __name__ == '__main__':
    main()