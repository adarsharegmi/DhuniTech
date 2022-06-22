from sanic import Blueprint
from dhuni_tech.skill_similarity.entrypoints import route_handler

similarity = Blueprint("similarity", url_prefix="api/v1/")

similarity.add_route(
    route_handler.get_similar_candidates, "similarity"
)