from __future__ import annotations
from sanic import Sanic

from ml_backend.ai_model.adapters import repository
from ml_backend.ai_model.domain import command, domain_handler, model
from ml_backend.ai_model.service_layers import unit_of_work
from ml_backend.ai_model.views import views
from ml_backend.ai_model.domain import events
from webapi.redis_config.redis_eventpublisher import publish
from ml_backend.ai_model.domain.exceptions import FILE_NAME_ALREADY_EXISTS


err = []
def check_app():
    try:
        app = Sanic.get_app("MlBackend")
    except Exception:
        app = Sanic("MlBackend")
    return app

async def add_ai_model(
    cmd: command.AddAIModel,
    uow: unit_of_work.AIModelSqlAlchemyUnitOfWork,
):
    async with uow:
        app = check_app()
        ai_model = await domain_handler.add_ai_model(cmd)
        # ai_model_name_res = await views.check_ai_model_name(cmd.name, app.ctx.db)
        # err.clear()
        # if ai_model_name_res:
        #     raise FILE_NAME_ALREADY_EXISTS()

        await uow.repository.add(ai_model)
    return ai_model.id_


async def update_ai_model(
    cmd: command.UpdateAIModel,
    uow: unit_of_work.AIModelSqlAlchemyUnitOfWork,
):
    async with uow:
        ai_model = await uow.repository.get(cmd.id_)
        app = check_app()
        ai_model_name_res = await views.check_ai_model_name_update(
            cmd.id_,
            cmd.name,
            app.ctx.db,
        )
        err.clear()
        if ai_model_name_res:
            raise FILE_NAME_ALREADY_EXISTS()
        
        source_components={
            "file_upload":"FileUpload",
            "streaming":"Streaming",
            "db_pull":"DBPull"
        }

        val = list(source_components.keys())[list(source_components.values()).index(ai_model["source"])]
        t = ai_model["source"]
        val_t = ai_model[t]
        ai_model["source"]=val+val_t
        ai_model = model.AIModel(
            id_=ai_model["id"],
            name=ai_model["name"],
            placement_name=ai_model["placement_name"],
            source=ai_model["source"],
            effective_from=ai_model["effective_from"],
            effective_to=ai_model["effective_to"],
            status=ai_model["status"],
        )
        ai_model_command = command.UpdateAIModel(
            ai_model=ai_model,
            id_=str(ai_model.id_),
            name=cmd.name if cmd.name else ai_model.name,
            placement_name = cmd.placement_name if cmd.placement_name else ai_model.placement_name,
            source = cmd.source if cmd.source else ai_model.source,
            effective_from = cmd.effective_from if cmd.effective_from else ai_model.effective_from,
            effective_to = cmd.effective_to if cmd.effective_to else ai_model.effective_to,
            status = cmd.status if cmd.status else ai_model.status,
            
        )
   
        ai_model = await domain_handler.update_ai_model(cmd=ai_model_command)
        await uow.repository.update(ai_model)


async def change_ai_model_status(
    cmd: command.ChangeAIModelStatus,
    uow: unit_of_work.AIModelSqlAlchemyUnitOfWork,
):
    await uow.repository.change_ai_model_status(cmd.ai_model_status, cmd.id_)

async def delete_ai_model(
    cmd:command.DeleteAIModel,
    uow: unit_of_work.AIModelSqlAlchemyUnitOfWork,
):
    await uow.repository.delete(cmd.id)