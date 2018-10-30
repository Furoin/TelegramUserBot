import config

for plugin in config.plugins:
    try:
        exec(f'from plugins import {plugin}')
    except Exception as e:
        print(e)

app = config.app

app.run()
