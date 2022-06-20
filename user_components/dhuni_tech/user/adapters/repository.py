import sqlalchemy as sa
from enum import Enum
from nepAddy_core.lib.repository import (
    Repository,
    SqlAlchemyRepository,
)
from nepAddy_core.lib.repository import DbConnection
from ml_backend.ai_model.domain import model
from ml_backend.ai_model.adapters.orm import (
    ai_model
)


class AIModel(Repository):
    async def add(self, model):
        return await super().add(model)

    async def get(self, ref):
        return await super().get(ref)


class AIModelRepository(SqlAlchemyRepository):
    def __init__(self, db: DbConnection):
        self.db = db

    async def _add(
        self,
        model: model.AIModel,
    ):
        ai_model_query = ai_model.insert()
        ai_model_values = {
            "id": str(model.id_),
            "name":model.name,
            "placement_name":model.placement_name,
            "effective_from":model.effective_from,
            "effective_to":model.effective_to,
            "status":model.status
        }
        source_components={
            "file_upload":"FileUpload",
            "streaming":"Streaming",
            "db_pull":"DBPull"
        }
        source = model.source.split(":")[0]
        val = model.source.split(":")[1]
        source_ = source_components.get("source","")
        other_c = source_components.keys().remove(source_)
        for k in other_c:
            ai_model_values.update({k:''}) 
        ai_model_values.update({'source':source_, source_:val})
        await self.db.execute(query=ai_model_query, values=ai_model_values)

    async def get(self, ref: str):
        ai_model_query = sa.select(
            [
                ai_model.c.id_,
                ai_model.c.name,
                ai_model.c.placement_name,
                ai_model.c.source,
                ai_model.c.effective_from,
                ai_model.c.effective_to,
                ai_model.c.status,
                ai_model.c.DBPull,
                ai_model.c.Streaming, 
                ai_model.c.FileUpload
            ]
        ).where(ai_model.c.id == ref)
        ai_model_data = await self.db.fetch_one(query=ai_model_query)
        return ai_model_data

    async def update(self, model: model.AIModel):
        update_ai_model = ai_model.update().where(ai_model.c.id == str(model.id_))
        ai_model_values = {
            "name":model.name,
            "placement_name":model.placement_name,
            "effective_from":model.effective_from,
            "effective_to":model.effective_to,
            "status":model.status,
        }
        source_components={
            "file_upload":"FileUpload",
            "streaming":"Streaming",
            "db_pull":"DBPull"
        }
        source = model.source.split(":")[0]
        val = model.source.split(":")[1]
        source_ = source_components.get("source","")
        other_c = source_components.keys().remove(source_)
        for k in other_c:
            ai_model_values.update({k:''}) 
            
        ai_model_values.update({'source':source_, source_:val})
        await self.db.execute(
            query=update_ai_model,
            values=ai_model_values,
        )

    async def change_ai_model_status(self, ai_model_status: Enum, id_: str):
        await self.db.execute(
            query=ai_model.update().where(ai_model.c.id == id_),
            values={"ai_model_status": ai_model_status},
        )
        
    async def delete(self, id: str): 
        await self.db.execute(ai_model.delete().where(ai_model.c.id==str(id)))