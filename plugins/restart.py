from pyrogram import Client, Filters
import config
import os
import sys

user_id = Client.user_id
prefix = config.prefix


@Client.on_message(Filters.user(user_id) & Filters.command("restart", prefix))
def restart(client, message):
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()
