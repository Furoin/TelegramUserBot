from pyrogram import Filters
import config

app = config.app
user_id = config.user_id
prefix = config.prefix

if config.language == "english":
    from languages.english import info_chat_text, info_text


@app.on_message(Filters.user(user_id) & Filters.command("info", prefix))
def info(client, message):
    if message.reply_to_message:
        text = info_text.format(message.reply_to_message.from_user.first_name,
                                message.reply_to_message.from_user.username,
                                message.reply_to_message.from_user.id)

        client.edit_message_text(message.chat.id, message.message_id, text, parse_mode="MARKDOWN")
    else:
        text = info_chat_text.format(message.chat.title,
                                     message.chat.username,
                                     message.chat.type,
                                     message.chat.id)
        client.edit_message_text(message.chat.id, message.message_id, text, parse_mode="MARKDOWN")
