from nepAddy_core.lib import unit_of_work
from nepAddy_core.lib.db_connection import DbConnection
from nepAddy_core.lib import repository
import typing


class CandidateSqlAlchemyUnitOfWork(unit_of_work.SqlAlchemyUnitOfWork):
    def __init__(
        self,
        connection: DbConnection,
        repository_class: typing.Type[repository.SqlAlchemyRepository],
    ):
        super().__init__(connection, repository_class)

class CandidateSkillsSqlAlchemyUnitOfWork(unit_of_work.SqlAlchemyUnitOfWork):
    def __init__(
        self,
        connection: DbConnection,
        repository_class: typing.Type[repository.SqlAlchemyRepository],
    ):
        super().__init__(connection, repository_class)