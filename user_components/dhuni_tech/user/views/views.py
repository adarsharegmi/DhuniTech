from uuid import UUID
import sqlalchemy as sa
from ml_backend.ai_model.adapters.orm import (
    ai_model,
)
from nepAddy_core.lib.db_connection import DbConnection
# from ml_backend.authentication.utils.auth_decorator import authorize
from ml_backend.placement.adapters.orm import placement

async def get_ai_model(id_: UUID, db: DbConnection):
    ai_model_query = sa.select(
        [
            ai_model.c.id,
            ai_model.c.name,
            placement.c.name.label("placement_name"),
            ai_model.c.source,
            ai_model.c.effective_from,
            ai_model.c.effective_to,
            ai_model.c.status,
        ]
    ).where(sa.and_(ai_model.c.id == id_,  ai_model.c.placement_name==placement.c.id))
    # , ai_model.c.ai_model_status == "ACTIVE"
    ai_model_result = await db.fetch_one(query=ai_model_query)
    return ai_model_result


async def check_ai_model_name(name: str, db: DbConnection):
    ai_model_query = sa.select(
        [sa.exists().where(sa.func.lower(ai_model.c.name) == sa.func.lower(name))]
    )
    ai_model_result = await db.fetch_val(query=ai_model_query)
    return ai_model_result


async def check_ai_model_name_update(id_: str, name: str, db: DbConnection):
    ai_model_query = sa.select(
        [
            sa.exists().where(
                sa.and_(
                    sa.func.lower(ai_model.c.name) == sa.func.lower(name),
                    ai_model.c.id != id_,
                )
            )
        ]
    )
    ai_model_result = await db.fetch_val(query=ai_model_query)
    return ai_model_result

async def get_all_ai_model(db: DbConnection):
    ai_model_query = sa.select(
        [
            ai_model.c.id,
            ai_model.c.name,
            placement.c.name.label("placement_name"),
            ai_model.c.source,
            ai_model.c.effective_from,
            ai_model.c.effective_to,
            ai_model.c.status
        ]
    ).where(ai_model.c.placement_name==placement.c.id)
    #.where(ai_model.c.ai_model_status == "ACTIVE")
    ai_model_result = await db.fetch_all(query=ai_model_query)
    return ai_model_result