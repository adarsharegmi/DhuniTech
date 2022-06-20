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