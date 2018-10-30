from pyrogram import Filters
from pyrogram.api.functions.messages import Search
from pyrogram.api.types import InputMessagesFilterEmpty
import config
import time

app = config.app
user_id = config.user_id
prefix = config.prefix

if config.language == "english":
    from languages.english import purge_me_text


@app.on_message(Filters.user(user_id) & Filters.command("purgeme", prefix))
def purgeme(client, message):
    if len(message.command) > 1:
        try:
            count = int(message.command[1])
        except ValueError:
            pass
        else:
            try:
                to_del = [message.id for message in app.send(
                    Search(peer=app.resolve_peer(message.chat.id), q="",
                           filter=InputMessagesFilterEmpty(),
                           min_date=0, max_date=0, offset_id=0, add_offset=0, limit=count,
                           max_id=0, min_id=0, hash=0,
                           from_id=app.resolve_peer(user_id)))["messages"]]
                i = len(to_del)
                client.delete_messages(message.chat.id, to_del)
                destruct = client.send_message(message.chat.id, purge_me_text.format(i))
                time.sleep(2)
                destruct.delete()
            except Exception as e:
                print(e)
    else:
        try:
            to_del = [message.id for message in app.send(
                Search(peer=app.resolve_peer(message.chat.id), q="",
                       filter=InputMessagesFilterEmpty(),
                       min_date=0, max_date=0, offset_id=0, add_offset=0, limit=100,
                       max_id=0, min_id=0, hash=0,
                       from_id=app.resolve_peer(user_id)))["messages"]]
            i = len(to_del)
            client.delete_messages(message.chat.id, to_del)
            destruct = client.send_message(message.chat.id, purge_me_text.format(i))
            time.sleep(2)
            destruct.delete()
        except Exception as e:
            print(e)
