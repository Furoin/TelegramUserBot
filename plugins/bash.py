from pyrogram import Filters
import config
import subprocess

app = config.app
user_id = config.user_id
prefix = config.prefix

if config.language == "english":
    from languages.english import bash_running_text, bash_text


@app.on_message(Filters.user(user_id) & Filters.command("bash", prefix))
def bash(client, message):
    if len(message.command) > 1:
        colength = len("bash") + len(prefix)
        code = message.text[colength:].lstrip()
        client.edit_message_text(message.chat.id, message.message_id, bash_running_text.format(code), parse_mode="HTML")
        try:
            result = subprocess.run(message.command[1:], stdout=subprocess.PIPE)
            result = str(result.stdout.decode())
            if not result:
                result = "No result!"
            else:
                result = result.strip()
        except Exception as e:
            result = str(e)
        final = bash_text.format(code, result)
        client.edit_message_text(message.chat.id, message.message_id, final, parse_mode="HTML")
