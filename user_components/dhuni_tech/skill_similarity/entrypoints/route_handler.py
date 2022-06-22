from uuid import UUID
from sanic import response
from nepAddy_core.lib.json_encoder import jsonable_encoder
from dhuni_tech.candidate.views import views as c_views
from dhuni_tech.job.views import views as j_views
from user_components.dhuni_tech.candidate import views

# for similar user
async def get_similar_candidates(request):
    name = request.json['name']
    job_skills = await j_views.get_job_skills_by_name(name, request.app.ctx.db)
    candidates = await c_views.get_all_candidate(request.app.ctx.db)
    jobs = jsonable_encoder(job_skills)
    candidates = jsonable_encoder(candidates)
    skills_req = set()
    candidates_skills = {}
    for i in jobs:
        skills_req.add(i["skills_name"].title())

    for i in candidates:
        candidate_skills = set()
        records = await c_views.get_candidate_skills(i['id'], request.app.ctx.db)
        result = jsonable_encoder(records)
        for single_record in result:
            candidate_skills.add(str(single_record['skills_name']).title())

        candidates_skills[i['id']] = len(list(candidate_skills.intersection(skills_req)))
    
    sorted_data = dict(sorted(candidates_skills.items(), key=lambda item: item[1], reverse=True))
    final = []
    for single in sorted_data:
        result = jsonable_encoder(await c_views.get_candidate(single, request.app.ctx.db))
        final.append({"user_id":single,"name":result["first_name"] + " "+result["last_name"], "score":sorted_data[single]})

    return response.json(
                    {
                        "candidate": final,
                    },
                    status=201,
                )
     