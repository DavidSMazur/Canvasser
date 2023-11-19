import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
import numpy as np
import certifi

import dotenv

dotenv.load_dotenv()

ca = certifi.where()

def get_db():
    uri = os.getenv('MONGO_COLLECTION_STRING')
    client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=ca)
    db = client.MHacks
    return db

loader = PyMuPDFLoader("Quasixenon.pdf")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=512, chunk_overlap=10)
docs = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()


db = get_db()
client = db.client  # Get the MongoClient object
# collection_name = "embeddings"
collection_name = "embeddings"

collection = db[collection_name]
index_name = "default"

vectordb = MongoDBAtlasVectorSearch.from_documents(
    docs, 
    embeddings,
    collection=collection,
    index_name=index_name
)

query = "What is a quasixenon?"
docs = vectordb.similarity_search(query)
print(docs[0].page_content)
