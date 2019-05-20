from sanic import Sanic
from sanic.response import json


#LOGGING_CONFIG='debug'
#app = Sanic('test', logging=LOGGING_CONFIG)
app = Sanic('test')
app.config.from_envvar('MYAPP_SETTINGS')

@app.route("/")
async def test(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
