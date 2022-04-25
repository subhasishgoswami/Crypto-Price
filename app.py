import requests
import os
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
  
updater = Updater("5360120330:AAFJIGQWcycGRq9bMg70zAvObC3Und3LoGQ",
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /Price - To get the price of token write /price Token Name""")
  
  
def price(update: Update, context: CallbackContext):
    url = 'https://rest.coinapi.io/v1/exchangerate/' + str(context.args[0]) + "/" + 'USD'
    headers = {'X-CoinAPI-Key' : os.environ['KEY']}
    response = requests.get(url, headers=headers)
    print(response.json()['rate'])
    update.message.reply_text("Price of" + " " + str(context.args[0]) + " is "+
        str(response.json()['rate']) + " USD")
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('price', price))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
  
updater.start_polling()



