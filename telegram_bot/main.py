import os
from typing import Final

from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters, CommandHandler, Application

import api_key

TOKEN: Final = os.environ.get('API_KEY')
BOT_USERNAME: Final = '@KRAKEN'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Type something random to get started!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('If you need help, you should ask for it in Google!')


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello there' in processed:
        return 'General Kenobi'

    if 'how are you' in processed:
        return 'I am good!'

    if 'youtube' in processed:
        return 'KRAKEN URL => https://www.youtube.com/@KRAKEN_GUR'

    return 'I do not understand what you wrote...'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('bot started...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
