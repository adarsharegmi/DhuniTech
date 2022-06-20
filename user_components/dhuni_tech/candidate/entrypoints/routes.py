from sanic import Blueprint
from ml_backend.candidate.entrypoints import route_handler

candidate = Blueprint("candidate", url_prefix="api/v1/")

candidate.add_route(
    route_handler.CandidateView.as_view(),
    "candidate/<id_>",
)

candidate.add_route(
    route_handler.get_candidate,
    "candidate",
)


candidate_skills = Blueprint("candidate_skills", url_prefix="api/v1/")

candidate_skills.add_route(
    route_handler.CandidateSkillsView.as_view(),
    "candidate_skills/<id_>",
)

candidate_skills.add_route(
    route_handler.get_candidate_skills,
    "candidate_skills",
)