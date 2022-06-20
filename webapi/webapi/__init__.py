from atexit import register
from sanic import Sanic
from webapi.bootstrap import init_database


app = Sanic("DhuniTech", register=True)


async def create_app(settings: None):
    db = init_database(settings)
    app.ctx.settings = settings
    app.ctx.db = db
    return app