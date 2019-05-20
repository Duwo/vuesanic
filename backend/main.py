from sanic import Sanic
from sanic import response

#LOGGING_CONFIG='debug'
#app = Sanic('test', logging=LOGGING_CONFIG)
app = Sanic('test')
app.config.from_envvar('MYAPP_SETTINGS')

@app.route("/")
async def test(request):
    return response.json(
            {"hello": "world"},
            headers={"Access-Control-Allow-Origin": "http://localhost:8080"},
            content_type="application/json",
            status=200
            )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
