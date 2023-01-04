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
    sql = "SELECT * FROM url;"
    return list(psql.execute_sql(sql))


@app.post("/v1/url/")
async def post_url(url: str):
    sql = f"""
        INSERT INTO url (\"date\", \"url\")
        VALUES ('{datetime.today().strftime('%Y-%m-%d')}', '{url}');
    """
    psql.execute_sql(sql)


@app.delete("/v1/url/")
async def delete_url(url: str):
    sql = f"DELETE FROM url WHERE url = '{url}';"
    psql.execute_sql(sql)


@app.get("/v1/tag/")
async def get_tag(url_id: int):
    sql = f"SELECT * FROM tag WHERE url_id = {url_id};"
    return list(psql.execute_sql(sql))


@app.post("/v1/tag/")
async def post_tag(url_id: int, tag: str):
    sql = f"""
        INSERT INTO tag (\"url_id\", \"date\", \"tag\") 
        VALUES ('{url_id}', '{datetime.today().strftime('%Y-%m-%d')}', '{tag}');
    """
    psql.execute_sql(sql)


@app.delete("/v1/tag/")
async def delete_url(url_id: int):
    sql = f"DELETE FROM tag WHERE url_id = '{url_id}';"
    psql.execute_sql(sql)


@app.get("/v1/alias/")
async def get_tag(url_id: int):
    sql = f"SELECT * FROM alias WHERE url_id = {url_id};"
    return list(psql.execute_sql(sql))


@app.post("/v1/alias/")
async def post_tag(url_id: int, tag: str):
    sql = f"""
        INSERT INTO alias (\"url_id\", \"date\", \"alias\") 
        VALUES ('{url_id}', '{datetime.today().strftime('%Y-%m-%d')}', '{tag}');
    """
    psql.execute_sql(sql)


@app.delete("/v1/alias/")
async def delete_url(url_id: int):
    sql = f"DELETE FROM alias WHERE url_id = '{url_id}';"
    psql.execute_sql(sql)


@app.get("/v1/rate/")
async def get_tag():
    sql = f"SELECT * FROM alias;"
    return list(psql.execute_sql(sql))


@app.post("/v1/rate/")
async def post_tag(url_id: int, tag: str):
    sql = f"""
        INSERT INTO alias (\"url_id\", \"date\", \"alias\") 
        VALUES ('{url_id}', '{datetime.today().strftime('%Y-%m-%d')}', '{tag}');
    """
    psql.execute_sql(sql)


@app.delete("/v1/rate/")
async def delete_url(url_id: int):
    sql = f"DELETE FROM alias WHERE url_id = '{url_id}';"
    psql.execute_sql(sql)


@app.get("/v1/list/")
async def get_list():
    sql = f"""
        SELECT alias, url.*, tag 
        FROM url 
        LEFT OUTER JOIN tag 
        ON url.id = tag.url_id 
        LEFT OUTER JOIN alias 
        ON url.id = alias.url_id;
    """
    return list(psql.execute_sql(sql))
