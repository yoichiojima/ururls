import pandas as pd
import sqlalchemy


class PostgresClient:
    def __init__(
        self,
        user: str,
        password: str,
        database: str,
        host: str = "localhost",
        port: int = 5432,
    ):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.port = port

    def __repr__(self):
        return (
            f"Postgres(user={self.user}, password={self.password}, "
            f"host={self.host}, port={self.port}, database={self.database})"
        )

    def create_engine(self) -> sqlalchemy.engine:
        return sqlalchemy.create_engine(
            f"postgresql://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.database}"
        )

    def execute_sql(self, sql: str):
        with self.create_engine().connect() as connection:
            return connection.execute(sql)
