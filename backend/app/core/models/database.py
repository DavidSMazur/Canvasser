from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import dotenv
import certifi
ca = certifi.where()

dotenv.load_dotenv()


def ping_mongo():
    uri = os.getenv('MONGO_COLLECTION_STRING')
    print(uri)

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
