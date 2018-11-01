from pyrogram import Client

## Bot settings ##

api_id = 123456
api_hash = "0123456789abcdef0123456789abcdef"
language = "english"

app = Client(
    "account",
    api_id=api_id,
    api_hash=api_hash
)

# Automatically sets your user id

app.start()
user_id = app.get_me().id
app.stop()

# Set an error channel

log_channel = -1001249303594

# Enabled plugins

plugins = ["eval", "exec", "info", "purgeme", "urban", "bash", "restart"]

# Command prefix

prefix = "."
