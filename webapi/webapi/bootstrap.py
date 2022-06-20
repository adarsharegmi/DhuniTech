from databases import Database
from nepAddy_core.lib.settings import AbstractSettings

def init_database(settings: AbstractSettings) -> Database:
    return Database(settings.pg_dsn)
