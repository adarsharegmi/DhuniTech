import json
from uuid import UUID
from pydantic import ValidationError
from sanic import response
from sanic.views import HTTPMethodView
from nepAddy_core.lib import err_msg
from nepAddy_core.lib.json_encoder import jsonable_encoder
from webapi.messagebus import messagebus

from dhuni_tech.job.views import views
from dhuni_tech.job.adapters import repository
from dhuni_tech.job.domain import command, exceptions
from dhuni_tech.job.service_layers import abstract, unit_of_work

async def get_job(request):
    job = await views.get_all_job(request.app.ctx.db)
    return response.json(jsonable_encoder(job))
        
class JobView(HTTPMethodView):
    async def get(self, request, id_):

        if   len(id_) > 2:
            job_result = await views.get_job(id_, request.app.ctx.db)

            if job_result is None:
                return response.json({"error": err_msg.DATA_NOT_FOUND}, status=404)
            return response.json(
                {
                    "job": jsonable_encoder(job_result),
                }
            )
        job = await views.get_all_job(request.app.ctx.db)
        return response.json(jsonable_encoder(job))
        
    async def post(self, request, id_=None):
        try:        
            err =[]
            validated_data = abstract.AddJob(**request.json)
            job_command = command.AddJob(**validated_data.dict())
            uow = unit_of_work.JobSqlAlchemyUnitOfWork(
                connection=request.app.ctx.db,
                repository_class=repository.JobRepository,
            )
            

            result = await messagebus.handle(message=job_command, uow=uow)
            
        except ValidationError as err:
            return response.json(json.loads(err.json()), status=400)

        except exceptions.DUPLICATE_JOB_FOUND as err:
                return response.json("Job already in database", status=400)
        if isinstance(result[0], UUID):
            job_result = await views.get_job(result[0], request.app.ctx.db)
            return response.json(
                {
                    "job": jsonable_encoder(job_result),
                },
                status=201,
            )
        return response.json(result[0], status=400)
    
    async def put(self, request, id_):
        if id_:
            try:
                validated_data = abstract.UpdateJob(id_=id_, **request.json)
                result = await messagebus.handle(
                    message=command.UpdateJob(**validated_data.dict()),
                    uow=unit_of_work.JobSqlAlchemyUnitOfWork(
                        connection=request.app.ctx.db,
                        repository_class=repository.JobRepository,
                    ),
                )
            except ValidationError as err:
                return response.json(json.loads(err.json()), status=400)
            except exceptions.DUPLICATE_JOB_FOUND as err:
                return response.json("Job already in database", status=400)
            if result:
                job_result = await views.get_job(id_, request.app.ctx.db)
                return response.json(
                    {
                        "job": jsonable_encoder(job_result),
                    },
                    status=201,
                )
            return response.json(result, status=400)
        return response.json({"error": "url not found"}, status=400)
    
    async def delete(self, request, id_):
    
        if id_:
            try:
                validated_data = abstract.DeleteJob(id=id_)
                result = await messagebus.handle(
                    message=command.DeleteJob(**validated_data.dict()),
                    uow=unit_of_work.JobSqlAlchemyUnitOfWork(
                        connection=request.app.ctx.db,
                        repository_class=repository.JobRepository,
                    ),
                )
            except ValidationError as err:
                return response.json(json.loads(err.json()), status=400)
            if result:
                return response.json(
                    {
                        "job": 'job deleted successfully',
                    },
                    status=201,
                )
            return response.json(result, status=400)
        return response.json({"error": "url not found"}, status=400)


async def get_job_skills(request):
    job_skills = await views.get_all_job_skills(request.app.ctx.db)
    return response.json(jsonable_encoder(job_skills))
        
class JobSkillsView(HTTPMethodView):

    async def get(self, request, id_):

        if   len(id_) > 2:
            job_result = await views.get_job_skills(id_, request.app.ctx.db)

            if job_result is None:
                return response.json({"error": err_msg.DATA_NOT_FOUND}, status=404)
            return response.json(
                {
                    "job": jsonable_encoder(job_result),
                }
            )
        job = await views.get_all_job_skills(request.app.ctx.db)
        return response.json(jsonable_encoder(job))
        
    async def post(self, request, id_=None):
        
        try:
            validated_data = abstract.AddJobSkills(**request.json)
            job_skills_command = command.AddJobSkills(**validated_data.dict())
            uow = unit_of_work.JobSqlAlchemyUnitOfWork(
                connection=request.app.ctx.db,
                repository_class=repository.JobSkillsRepository,
            )
            result = await messagebus.handle(message=job_skills_command, uow=uow)
            
        except ValidationError as err:
            return response.json(json.loads(err.json()), status=400)
        except exceptions.DUPLICATE_SKILL_FOUND as err:
            return response.json(json.loads(err.json()), status=400)
        except Exception as e:
                return response.json("duplicate skill found", status=400)
        if isinstance(result[0], UUID):
            job_result = await views.get_job_skills_by_id(result[0], request.app.ctx.db)
            return response.json(
                {
                    "job": jsonable_encoder(job_result),
                },
                status=201,
            )
        return response.json(result[0], status=400)
    
    async def put(self, request, id_):
        if id_:
            try:
                validated_data = abstract.UpdateJobSkills(id_=id_, **request.json)
                result = await messagebus.handle(
                    message=command.UpdateJobSkills(**validated_data.dict()),
                    uow=unit_of_work.JobSqlAlchemyUnitOfWork(
                        connection=request.app.ctx.db,
                        repository_class=repository.JobSkillsRepository,
                    ),
                )
            except ValidationError as err:
                return response.json(json.loads(err.json()), status=400)

            except exceptions.DUPLICATE_SKILL_FOUND as err:
                return response.json(json.loads(err.json()), status=400)
            except Exception as e:
                return response.json("duplicate skill found", status=400)

            if result:
                job_result = await views.get_job_skills_by_id(id_, request.app.ctx.db)
                return response.json(
                    {
                        "job": jsonable_encoder(job_result),
                    },
                    status=201,
                )
            return response.json(result, status=400)
        return response.json({"error": "url not found"}, status=400)
    
    async def delete(self, request, id_):
        if id_:
            try:
                validated_data = abstract.DeleteJobSkills(id=id_)
                result = await messagebus.handle(
                    message=command.DeleteJobSkills(**validated_data.dict()),
                    uow=unit_of_work.JobSkillsSqlAlchemyUnitOfWork(
                        connection=request.app.ctx.db,
                        repository_class=repository.JobSkillsRepository,
                    ),
                )
            except ValidationError as err:
                return response.json(json.loads(err.json()), status=400)
            if result:
                return response.json(
                    {
                        "job": 'job skills deleted successfully',
                    },
                    status=201,
                )
            return response.json(result, status=400)
        return response.json({"error": "url not found"}, status=400)