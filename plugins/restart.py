from pyrogram import Filters
import config
import os
import sys

app = config.app
user_id = config.user_id
prefix = config.prefix


@app.on_message(Filters.user(user_id) & Filters.command("restart", prefix))
def restart(client, message):
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()
