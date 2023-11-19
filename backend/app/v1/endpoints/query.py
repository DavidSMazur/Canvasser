# /v1/endpoints/query.py
from pydantic import BaseModel

from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
import os
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.embeddings.openai import OpenAIEmbeddings
import json


from fastapi import APIRouter
import dotenv

dotenv.load_dotenv()
ca = certifi.where()

router = APIRouter()


# Define the request model
class QueryRequest(BaseModel):
    course_id: str
    query_text: str


def get_db():
    uri = os.getenv('MONGO_COLLECTION_STRING')
    client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=ca)
    db = client.MHacks
    return db


@router.post("/")
async def query(request: QueryRequest):
    embeddings = OpenAIEmbeddings()


    db = get_db()
    client = db.client  # Get the MongoClient object
    collection_name = "embeddings"

    collection = db[collection_name]
    index_name = "default"



    query = request.query_text
    # print(embeddings.embed_query(query))

    results = collection.aggregate([
      {"$vectorSearch": {
        "queryVector": embeddings.embed_query(query),
        "path": "embedding",
        "numCandidates": 100,
        "limit": 4,
        "index": "default",
          }}
    ])


# Convert the CommandCursor to a list and then to a string
    results_list = list(results)
    print(results_list[0].get("text"))
    # results_str = str(results_list)

    # print(json.dumps(str(results_list)))
    # for document in results:
    #     print(document.text)

    return {"response": results_list[0].get("text")}


# @router.post("/", response_model=ItemSchema)
# async def create_item(item: ItemSchema):
#     return item
