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


@app.get("/v1/url/", tags=["url"])
async def get_urls():
    sql = "SELECT * FROM url;"
    return list(psql.execute_sql(sql))


@app.post("/v1/url/", tags=["url"])
async def post_url(url: str):
    sql = f"""
        INSERT INTO url (\"date\", \"url\")
        VALUES ('{datetime.today().strftime('%Y-%m-%d')}', '{url}');
    """
    psql.execute_sql(sql)


@app.put("/v1/url/", tags=["url"])
async def post_url(url_id: int, url: str):
    sql = f"""
        UPDATE 
            url 
        SET 
            \"date\" = '{datetime.today().strftime('%Y-%m-%d')}', 
            \"url\" = '{url}'
        WHERE 
            id = '{url_id}';
    """
    psql.execute_sql(sql)


@app.delete("/v1/url/", tags=["url"])
async def delete_url(url: str):
    sql = f"DELETE FROM url WHERE url = '{url}';"
    psql.execute_sql(sql)


@app.get("/v1/tag/", tags=["tag"])
async def get_tag():
    sql = f"SELECT * FROM tag;"
    return list(psql.execute_sql(sql))


@app.post("/v1/tag/", tags=["tag"])
async def post_tag(url_id: int, tag: str):
    sql = f"""
        INSERT INTO tag (\"url_id\", \"date\", \"tag\") 
        VALUES ('{url_id}', '{datetime.today().strftime('%Y-%m-%d')}', '{tag}');
    """
    psql.execute_sql(sql)


@app.put("/v1/tag/", tags=["tag"])
async def post_url(_id: int, tag: str):
    sql = f"""
        UPDATE 
            tag 
        SET 
            \"date\" = '{datetime.today().strftime('%Y-%m-%d')}', 
            \"tag\" = '{tag}'
        WHERE 
            id = '{_id}';
    """
    psql.execute_sql(sql)


@app.delete("/v1/tag/", tags=["tag"])
async def delete_url(url_id: int):
    sql = f"DELETE FROM tag WHERE url_id = '{url_id}';"
    psql.execute_sql(sql)


@app.get("/v1/alias/", tags=["alias"])
async def get_tag():
    sql = f"SELECT * FROM alias;"
    return list(psql.execute_sql(sql))


@app.post("/v1/alias/", tags=["alias"])
async def post_tag(url_id: int, alias: str):
    sql = f"""
        INSERT INTO alias (\"url_id\", \"date\", \"alias\") 
        VALUES ('{url_id}', '{datetime.today().strftime('%Y-%m-%d')}', '{alias}');
    """
    psql.execute_sql(sql)


@app.put("/v1/alias/", tags=["alias"])
async def post_url(url_id: int, alias: str):
    sql = f"""
        UPDATE 
            alias 
        SET 
            \"date\" = '{datetime.today().strftime('%Y-%m-%d')}', 
            \"alias\" = '{alias}'
        WHERE 
            url_id = '{url_id}';
    """
    psql.execute_sql(sql)


@app.delete("/v1/alias/", tags=["alias"])
async def delete_url(url_id: int):
    sql = f"DELETE FROM alias WHERE url_id = '{url_id}';"
    psql.execute_sql(sql)


@app.get("/v1/rate/", tags=["rate"])
async def get_tag():
    sql = f"SELECT * FROM rate;"
    return list(psql.execute_sql(sql))


@app.put("/v1/rate/", tags=["rate"])
async def post_url(url_id: int, rate: int):
    sql = f"""
        UPDATE 
            rate 
        SET 
            \"date\" = '{datetime.today().strftime('%Y-%m-%d')}', 
            \"rate\" = '{rate}'
        WHERE 
            url_id = '{url_id}';
    """
    psql.execute_sql(sql)


@app.post("/v1/rate/", tags=["rate"])
async def post_tag(url_id: int, rate: int):
    sql = f"""
        INSERT INTO rate (\"url_id\", \"date\", \"rate\") 
        VALUES ('{url_id}', '{datetime.today().strftime('%Y-%m-%d')}', {rate});
    """
    psql.execute_sql(sql)


@app.delete("/v1/rate/", tags=["rate"])
async def delete_url(url_id: int):
    sql = f"DELETE FROM rate WHERE url_id = '{url_id}';"
    psql.execute_sql(sql)


@app.get("/v1/category/", tags=["category"])
async def get_tag():
    sql = f"SELECT * FROM category;"
    return list(psql.execute_sql(sql))


@app.put("/v1/category/", tags=["category"])
async def post_url(url_id: int, category: str):
    sql = f"""
        UPDATE 
            category 
        SET 
            \"date\" = '{datetime.today().strftime('%Y-%m-%d')}', 
            \"category\" = '{category}'
        WHERE 
            url_id = '{url_id}';
    """
    psql.execute_sql(sql)


@app.post("/v1/category/", tags=["category"])
async def post_tag(url_id: int, category: str):
    sql = f"""
        INSERT INTO category (\"url_id\", \"date\", \"category\") 
        VALUES ('{url_id}', '{datetime.today().strftime('%Y-%m-%d')}', '{category}');
    """
    psql.execute_sql(sql)


@app.delete("/v1/category/", tags=["category"])
async def delete_url(url_id: int):
    sql = f"DELETE FROM category WHERE url_id = '{url_id}';"
    psql.execute_sql(sql)


def query_one(_list: list, query: str) -> list:
    filtered_list = list(filter(lambda x: x[0] == query, _list))
    if filtered_list:
        return filtered_list[0][1]
    else:
        return []


def query_many(_list: list, query: str, key: str) -> list:
    filtered_list = list(filter(lambda x: x[0] == query, _list))
    if filtered_list:
        return [i[key] for i in filtered_list]
    else:
        return []


@app.get("/v1/summary_1", tags=["summary"])
async def get_summary():
    urls = list(psql.execute_sql("SELECT id, url FROM url;"))
    tags = list(psql.execute_sql("SELECT url_id, tag FROM tag;"))
    alias = list(psql.execute_sql("SELECT url_id, alias FROM alias;"))
    category = list(psql.execute_sql("SELECT url_id, category FROM category;"))

    res = []
    for i in urls:
        item = {}
        item["id"] = i[0]
        item["url"] = i[1]
        item["tags"] = query_many(tags, i[0], "tag")
        item["alias"] = query_one(alias, i[0])
        item["category"] = query_one(category, i[0])
        res.append(item)

    return res
