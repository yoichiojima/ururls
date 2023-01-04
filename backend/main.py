import os
from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from postgres_client import PostgresClient

app = FastAPI()

origins = ["http://localhost", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


load_dotenv()

psql = PostgresClient(
    user="readwrite_user",
    password=os.environ.get("POSTGRES_PASSWORD"),
    database=os.environ.get("POSTGRES_DATABASE"),
)


@app.get("/v1/url/")
async def get_urls():
    return [i for i in psql.execute_sql("SELECT * FROM url;")]


@app.post("/v1/url/")
async def post_url(url: str):
    psql.execute_sql(
        f"INSERT INTO url (\"date\", \"url\") VALUES ('{datetime.today().strftime('%Y-%m-%d')}', '{url}');"
    )


@app.delete("/v1/url/")
async def delete_url(url: str):
    psql.execute_sql(f"DELETE FROM url WHERE url = '{url}';")


@app.get("/v1/tag/")
async def get_tag(url_id: int):
    return [i for i in psql.execute_sql(f"SELECT * FROM tag WHERE url_id = {url_id};")]


@app.post("/v1/tag/")
async def post_tag(url_id: int, tag: str):
    psql.execute_sql(
        f"INSERT INTO tag (\"url_id\", \"date\", \"tag\") VALUES ('{url_id}', '{datetime.today().strftime('%Y-%m-%d')}', '{tag}');"
    )


@app.delete("/v1/tag/")
async def delete_url(url_id: int):
    psql.execute_sql(f"DELETE FROM tag WHERE url_id = '{url_id}';")


@app.get("/v1/alias/")
async def get_tag(url_id: int):
    return [
        i for i in psql.execute_sql(f"SELECT * FROM alias WHERE url_id = {url_id};")
    ]


@app.post("/v1/alias/")
async def post_tag(url_id: int, tag: str):
    psql.execute_sql(
        f"INSERT INTO alias (\"url_id\", \"date\", \"alias\") VALUES ('{url_id}', '{datetime.today().strftime('%Y-%m-%d')}', '{tag}');"
    )


@app.delete("/v1/alias/")
async def delete_url(url_id: int):
    psql.execute_sql(f"DELETE FROM alias WHERE url_id = '{url_id}';")

@app.get("/v1/list/")
async def get_list():
    result = psql.execute_sql("""
        SELECT alias, url.*, tag 
        FROM url 
        LEFT OUTER JOIN tag 
        ON url.id = tag.url_id 
        LEFT OUTER JOIN alias 
        ON url.id = alias.url_id;
    """)
    return list(result)