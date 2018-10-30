from pyrogram import Filters
import config
import urbandict as ud

app = config.app
user_id = config.user_id
prefix = config.prefix

if config.language == "english":
    from languages.english import urban_not_found_text, urban_text


@app.on_message(Filters.user(user_id) & Filters.command("urban", prefix))
def urban(client, message):
    if len(message.command) > 1:
        word = str(message.text)[6:].lstrip()
        try:
            mean = ud.define(word)
        except:
            client.send_message(message.chat.id, urban_not_found_text.format(word))
        else:
            if len(mean) >= 0:
                client.send_message(message.chat.id, urban_text.format(word, mean[0]['def'], mean[0]['example']))
            else:
                client.send_message(message.chat.id, urban_not_found_text.format(word))
