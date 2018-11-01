import config

for plugin in config.plugins:
    try:
        print("Starting Plugin: " + str(plugin))
        exec('import plugins.{}'.format(plugin))
    except Exception as e:
        print(e)

app = config.app

app.run()
