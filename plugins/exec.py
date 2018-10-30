from pyrogram import Filters
import config

app = config.app
user_id = config.user_id
prefix = config.prefix

if config.language == "english":
    from languages.english import exec_running_text, exec_error_text, exec_success_text, exec_result_text


@app.on_message(Filters.user(user_id) & Filters.command("exec", prefix))
def execute(c, m):
    colength = len("exec") + len(prefix)
    code = m.text[colength:].lstrip()
    c.edit_message_text(m.chat.id, m.message_id, exec_running_text.replace('{code}', code), parse_mode="HTML")
    try:
        exec('def __ex(c, m): ' + ''.join('\n ' + l for l in code.split('\n')))
        result = locals()['__ex'](c, m)

    except Exception as e:
        c.edit_message_text(m.chat.id, m.message_id, exec_error_text.replace('{code}', code).replace('{error}', str(e)), parse_mode="HTML")

    else:
        if result:
            c.edit_message_text(m.chat.id, m.message_id, exec_result_text.replace('{code}', code).replace('{result}', str(result)), parse_mode="HTML")

        else:
            c.edit_message_text(m.chat.id, m.message_id, exec_success_text.replace('{code}', code), parse_mode="HTML")


