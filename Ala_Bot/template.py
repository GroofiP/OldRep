import telegram
from telegram.ext import Updater, CommandHandler

from click import click_form
from constabot import TEXT_START, TEXT_HELP
from logleader import logger
from search.v1 import search_ps5, search_ps5_link

TOKEN = "1915695595:AAF0TDRKkdVFGol-qOLQULUKMi24smfPLCQ"

bot = telegram.Bot(token=TOKEN)


def start(update, context):
    """Send a message when the command /start is issued."""
    logger.info(start.__name__)
    logger.info(update.effective_chat)
    logger.info(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=TEXT_START)


def help_command(update, context):
    """Send a message when the command /help is issued."""
    logger.info(help_command.__name__)
    logger.info(update.effective_chat)
    logger.info(update.message.text)
    update.message.reply_text(TEXT_HELP)


def main():
    # Создает Updater и привязывает к боту
    updater = Updater(token=TOKEN)

    # Для работы функций
    dispatcher = updater.dispatcher

    # стандартные команды
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # пользовательские функции
    dispatcher.add_handler(CommandHandler("search", search_ps5))
    dispatcher.add_handler(CommandHandler("search_link", search_ps5_link))
    dispatcher.add_handler(CommandHandler("click", click_form))


    # стартуем бота
    updater.start_polling()


if __name__ == '__main__':
    main()
