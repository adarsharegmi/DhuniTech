from atexit import register
from sanic import Sanic
from webapi.bootstrap import init_database

from dhuni_tech.job.entrypoints.routes import job, job_skills
from dhuni_tech.candidate.entrypoints.routes import candidate, candidate_skills

app = Sanic("DhuniTech")

async def create_app(settings: None):
    app.blueprint(job)
    app.blueprint(job_skills)
    app.blueprint(candidate)
    app.blueprint(candidate_skills)
    db = init_database(settings)
    app.ctx.settings = settings
    app.ctx.db = db
    return app