import asyncpg

from LIB.DB import DB


class ClientDB(DB):
    def __init__(self, host: str, database: str, user: str, password: str):
        super().__init__(host, database, user, password)
