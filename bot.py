from pyrogram import Client

api_id = 123456
api_hash = "0123456789abcdef0123456789abcdef"

Client("account", api_id=api_id, api_hash=api_hash, plugins_dir="plugins").run()
