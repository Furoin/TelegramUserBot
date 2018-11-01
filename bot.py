import config

for plugin in config.plugins:
    try:
        exec('from plugins import {}'.format(plugin))
    except Exception as e:
        print(e)

app = config.app

app.run()
