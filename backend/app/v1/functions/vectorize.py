from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

from werkzeug.utils import secure_filename

import os
import dotenv

dotenv.load_dotenv()
# Use Azure OpenAI
# os.environ["OPENAI_API_TYPE"] = "azure"


def save_transcript_to_file(transcript):
    temp_file_path = os.path.join(os.getcwd(), "./TempTranscript.txt")

    with open(temp_file_path, 'w') as file:
        file.write(transcript)
    return temp_file_path

def upload_data_to_vector_db(textData, persist_directory):
    temp_file_path = save_transcript_to_file(textData)

    loader = TextLoader(temp_file_path)
    documents = loader.load()
    
    print("TFP: ", temp_file_path)


    try:
        # Split the document text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=150,
            chunk_overlap=0,
            separators=["\n\n", "\n", "(?<=\. )", " ", ""]
        )
        
        texts = text_splitter.split_documents(documents)

        print("Texts: ", texts)

        # Generate embeddings
        embeddings = OpenAIEmbeddings()

        # Store vectors in Chroma
        vectordb = Chroma.from_documents(documents=texts, 
                                        embedding=embeddings,
                                        persist_directory=persist_directory)
        vectordb.persist()


        document = documents[0]
        text_content = document.page_content
    finally:
        os.remove(temp_file_path)  # Delete the temporary file
    print(f"Embeddings for added to the vector database.")

    return text_content

current_dir = os.path.dirname(os.path.abspath(__file__))
persist_directory = os.path.join(current_dir, "storage")
upload_data_to_vector_db("Hello", persist_directory)
