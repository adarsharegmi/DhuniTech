from sanic import Blueprint
from ml_backend.job.entrypoints import route_handler

job = Blueprint("job", url_prefix="api/v1/")

job.add_route(
    route_handler.JobView.as_view(),
    "job/<id_>",
)

job.add_route(
    route_handler.get_job,
    "job",
)


job_skills = Blueprint("job_skills", url_prefix="api/v1/")

job_skills.add_route(
    route_handler.JobSkillsView.as_view(),
    "job_skills/<id_>",
)

job_skills.add_route(
    route_handler.get_job_skills,
    "job_skills",
)