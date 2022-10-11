import logging
from telegram.ext import Updater
from telegram import Update, ParseMode
from telegram.ext import CallbackContext, ContextTypes
from telegram.ext import CommandHandler, PollAnswerHandler
from data import PgsqlDataSource, MocDataSource
from data import Avocado
from os import environ

datasource = MocDataSource()
avocado = Avocado(datasource)
updater = Updater(token=environ.get('TG_BOT_TOKEN'), use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def avo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=avocado.__str__())
    logging.info(update.message.text)


def set_handlers():
    dispatcher.add_handler(CommandHandler('avocado', avo))
    dispatcher.add_handler(PollAnswerHandler(avo))


def main():
    set_handlers()
    updater.start_polling()


if __name__ == '__main__':
    main()
