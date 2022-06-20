from nepAddy_core.databases.entrypoint.console import AlembicCommand
from webapi.main import app

settings = app.ctx.settings


class CliCommand:
    def __init__(self):
        self.alembic = AlembicCommand(settings)
