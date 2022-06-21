import json
from uuid import UUID
from pydantic import ValidationError
from sanic import response
from sanic.views import HTTPMethodView

from nepAddy_core.lib import err_msg
from nepAddy_core.lib.json_encoder import jsonable_encoder
from webapi.messagebus import messagebus

from dhuni_tech.candidate.views import views
from dhuni_tech.candidate.adapters import repository
from dhuni_tech.candidate.domain import command, exceptions
from dhuni_tech.candidate.service_layers import abstract, unit_of_work

async def get_candidate(request):
    candidate = await views.get_all_candidate(request.app.ctx.db)
    return response.json(jsonable_encoder(candidate))
        
class CandidateView(HTTPMethodView):

    async def get(self, request, id_):

        if   len(id_) > 2:
            candidate_result = await views.get_candidate(id_, request.app.ctx.db)

            if candidate_result is None:
                return response.json({"error": err_msg.DATA_NOT_FOUND}, status=404)
            return response.json(
                {
                    "candidate": jsonable_encoder(candidate_result),
                }
            )
        candidate = await views.get_all_candidate(request.app.ctx.db)
        return response.json(jsonable_encoder(candidate))
        
    async def post(self, request, id_=None):
        
        try:
            validated_data = abstract.AddCandidate(**request.json)
            candidate_command = command.AddCandidate(**validated_data.dict())
            uow = unit_of_work.CandidateSqlAlchemyUnitOfWork(
                connection=request.app.ctx.db,
                repository_class=repository.CandidateRepository,
            )
            result = await messagebus.handle(message=candidate_command, uow=uow)
            
        except ValidationError as err:
            return response.json(json.loads(err.json()), status=400)

        if isinstance(result[0], UUID):
            candidate_result = await views.get_candidate(result[0], request.app.ctx.db)
            return response.json(
                {
                    "candidate": jsonable_encoder(candidate_result),
                },
                status=201,
            )
        return response.json(result[0], status=400)
    
    async def put(self, request, id_):
        if id_:
            try:
                validated_data = abstract.UpdateCandidate(id_=id_, **request.json)
                result = await messagebus.handle(
                    message=command.UpdateCandidate(**validated_data.dict()),
                    uow=unit_of_work.CandidateSqlAlchemyUnitOfWork(
                        connection=request.app.ctx.db,
                        repository_class=repository.CandidateRepository,
                    ),
                )
            except exceptions.FILE_NAME_ALREADY_EXISTS as err:
                return response.json(json.loads({'message':'file name already exists'}),
                                    status=500)
            except ValidationError as err:
                return response.json(json.loads(err.json()), status=400)
            if result:
                candidate_result = await views.get_candidate(id_, request.app.ctx.db)
                return response.json(
                    {
                        "candidate": jsonable_encoder(candidate_result),
                    },
                    status=201,
                )
            return response.json(result, status=400)
        return response.json({"error": "url not found"}, status=400)
    
    async def delete(self, request, id_):
    
        if id_:
            try:
                validated_data = abstract.DeleteCandidate(id=id_)
                result = await messagebus.handle(
                    message=command.DeleteCandidate(**validated_data.dict()),
                    uow=unit_of_work.CandidateSqlAlchemyUnitOfWork(
                        connection=request.app.ctx.db,
                        repository_class=repository.CandidateRepository,
                    ),
                )
            except ValidationError as err:
                return response.json(json.loads(err.json()), status=400)
            if result:
                return response.json(
                    {
                        "candidate": 'candidate deleted successfully',
                    },
                    status=201,
                )
            return response.json(result, status=400)
        return response.json({"error": "url not found"}, status=400)


# for skills

async def get_candidate_skills(request):
    candidate_skills = await views.get_all_candidate_skills(request.app.ctx.db)
    return response.json(jsonable_encoder(candidate_skills))
        
class CandidateSkillsView(HTTPMethodView):

    async def get(self, request, id_):

        if   len(id_) > 2:
            candidate_result = await views.get_candidate_skills(id_, request.app.ctx.db)

            if candidate_result is None:
                return response.json({"error": err_msg.DATA_NOT_FOUND}, status=404)
            return response.json(
                {
                    "candidate": jsonable_encoder(candidate_result),
                }
            )
        candidate = await views.get_all_candidate_skills(request.app.ctx.db)
        return response.json(jsonable_encoder(candidate))
        
    async def post(self, request, id_=None):
        
        try:
            validated_data = abstract.AddCandidateSkills(**request.json)
            candidate_skills_command = command.AddCandidateSkills(**validated_data.dict())
            uow = unit_of_work.CandidateSqlAlchemyUnitOfWork(
                connection=request.app.ctx.db,
                repository_class=repository.CandidateSkillsRepository,
            )
            result = await messagebus.handle(message=candidate_skills_command, uow=uow)
            
        except ValidationError as err:
            return response.json(json.loads(err.json()), status=400)

        if isinstance(result[0], UUID):
            candidate_result = await views.get_candidate_skills(result[0], request.app.ctx.db)
            return response.json(
                {
                    "candidate": jsonable_encoder(candidate_result),
                },
                status=201,
            )
        return response.json(result[0], status=400)
    
    async def put(self, request, id_):
        if id_:
            try:
                validated_data = abstract.UpdateCandidateSkills(id_=id_, **request.json)
                result = await messagebus.handle(
                    message=command.UpdateCandidateSkills(**validated_data.dict()),
                    uow=unit_of_work.CandidateSqlAlchemyUnitOfWork(
                        connection=request.app.ctx.db,
                        repository_class=repository.CandidateSkillsRepository,
                    ),
                )
            except ValidationError as err:
                return response.json(json.loads(err.json()), status=400)
            if result:
                candidate_result = await views.get_candidate_skills(id_, request.app.ctx.db)
                return response.json(
                    {
                        "candidate": jsonable_encoder(candidate_result),
                    },
                    status=201,
                )
            return response.json(result, status=400)
        return response.json({"error": "url not found"}, status=400)
    
    async def delete(self, request, id_):
        if id_:
            try:
                validated_data = abstract.DeleteCandidateSkills(id=id_)
                result = await messagebus.handle(
                    message=command.DeleteCandidateSkills(**validated_data.dict()),
                    uow=unit_of_work.CandidateSkillsSqlAlchemyUnitOfWork(
                        connection=request.app.ctx.db,
                        repository_class=repository.CandidateSkillsRepository,
                    ),
                )
            except ValidationError as err:
                return response.json(json.loads(err.json()), status=400)
            if result:
                return response.json(
                    {
                        "candidate": 'candidate skills deleted successfully',
                    },
                    status=201,
                )
            return response.json(result, status=400)
        return response.json({"error": "url not found"}, status=400)