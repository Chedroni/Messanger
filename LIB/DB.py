import asyncio
import asyncpg


class DB:
    def __init__(self, host: str, database: str, user: str, password: str):
        self.conn: asyncpg.Connection = await asyncpg.connect(host=host,
                                                              database=database,
                                                              user=user,
                                                              password=password)

        self.pool = asyncpg.create_pool(connection_class=self.conn)

    def request(self, query, records_count=-1) -> dict:
        async with self.pool.acquire(timeout=60) as conn:
            curs: asyncpg.connection.cursor.Cursor = await conn.cursor(query)
            result = await curs.fetch(records_count)
        return dict(result)
