import os
from pymongo import MongoClient


db_name = os.getenv("MONGO_DB")
if not db_name:
    raise RuntimeError("MONGO_DB não está definido no .env")

client = MongoClient(
    host=os.getenv("MONGO_HOST", "localhost"),
    port=int(os.getenv("MONGO_PORT", "27017")),
    username=os.getenv("MONGO_USER"),
    password=os.getenv("MONGO_PASSWORD"),
    authSource=os.getenv("MONGO_AUTH_SOURCE", "admin"),
)

db = client.get_database(db_name)
