from pyrogram import Filters
import config

app = config.app
user_id = config.user_id
prefix = config.prefix

if config.language == "english":
    from languages.english import eval_running_text, eval_error_text, eval_success_text, eval_result_text


@app.on_message(Filters.user(user_id) & Filters.command("eval", prefix))
def evalcode(c, m):
    colength = len("eval") + len(prefix)
    code = m.text[colength:].lstrip()
    c.edit_message_text(m.chat.id, m.message_id, eval_running_text.replace('{code}', code), parse_mode="HTML")
    try:
        result = eval(code)

    except Exception as e:
        c.edit_message_text(m.chat.id, m.message_id, eval_error_text.replace('{code}', code).replace('{error}', str(e)), parse_mode="HTML")

    else:
        if result:
            c.edit_message_text(m.chat.id, m.message_id, eval_result_text.replace('{code}', code).replace('{result}', str(result)), parse_mode="HTML")

        else:
            c.edit_message_text(m.chat.id, m.message_id, eval_success_text.replace('{code}', code), parse_mode="HTML")


