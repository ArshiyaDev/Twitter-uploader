import os
from telegram import Bot


def upload_to_telegram(bot_token, channel_id):
    telegram_bot = Bot(token=bot_token)

    for file in os.listdir("."):
        if file.endswith(".m4a"):
            with open(file, "rb") as audio_file:
                telegram_bot.send_audio(chat_id=channel_id, audio=audio_file)
