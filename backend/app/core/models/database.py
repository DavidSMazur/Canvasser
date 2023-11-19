from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi.responses import JSONResponse
import os
import dotenv
import certifi
import json
from bson import json_util
from bson.json_util import dumps

ca = certifi.where()

dotenv.load_dotenv()

def get_db():
    uri = os.getenv('MONGO_COLLECTION_STRING')
    client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=ca)
    db = client.Database
    return db

def ping_mongo():
    uri = os.getenv('MONGO_COLLECTION_STRING')

    # Set the Stable API version when creating a new client
    client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=ca)

    # Send a ping to confirm a successful connection
    try:
        response = client.MHacks.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return response
    except Exception as e:
        print(e)
    finally:
        client.close()


def retrieve_course():
    uri = os.getenv('MONGO_COLLECTION_STRING')
    client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=ca)
    db = client.MHacks
    collection = db.courses
    sample_json = {
        "course_id": 304,
        "assignment": [1, 3, 7, 9],
        "announcement": [4, 6, 9]
    }
    try:
        response = collection.insert_one(sample_json)
        # response = collection.find({"course_id": 301})
        print(response.inserted_id)
        return response.inserted_id
    except Exception as e:
        print(e)
    finally:
        client.close()
