import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot("YOUR_BOT_TOKEN")

# Destination chat ID where the messages will be forwarded
# Group and Channel ID is negative integer while User ID and Bot Id is positive integer
destination_chat_id = "SPECIFIED_DESTINATION_CHAT_ID"

# Delete the webhook before polling
bot.delete_webhook()

# Handle the /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hi! I'm an forwarder bot. Send me a message, and I'll forward it to the destination.")

# Handle the /status command
@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "I'm running and ready to forward messages.")

# Define a message handler to forward messages to the destination chat
@bot.message_handler(func=lambda message: True, content_types=['text', 'photo', 'audio', 'document', 'video', 'voice', 'sticker'])
def forward_message(message):
    if message.text:
        bot.send_message(destination_chat_id, message.text)
    elif message.photo:
        bot.send_photo(destination_chat_id, message.photo[-1].file_id)
    elif message.audio:
        bot.send_audio(destination_chat_id, message.audio.file_id)
    elif message.document:
        bot.send_document(destination_chat_id, message.document.file_id)
    elif message.video:
        bot.send_video(destination_chat_id, message.video.file_id)
    elif message.voice:
        bot.send_voice(destination_chat_id, message.voice.file_id)
    elif message.sticker:
        bot.send_sticker(destination_chat_id, message.sticker.file_id)
    elif message.video_note:
        bot.send_video_note(destination_chat_id, message.video_note.file_id)

# Start polling
bot.polling()