import os
from pprint import pprint

from dotenv import load_dotenv
from postgres_client import PostgresClient

load_dotenv()

psql = PostgresClient(
    user="readwrite_user",
    password=os.environ.get("POSTGRES_PASSWORD"),
    database=os.environ.get("POSTGRES_DATABASE"),
)
# print("\nurls")
# pprint(urls)
# print("")

# print("\nytags")
# pprint(tags)
# print("")

# print("\naliases")
# pprint(aliases)
# print("")

# print("\ncategory")
# pprint(category)
# print("")
