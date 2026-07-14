from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

import os
from dotenv import load_dotenv

load_dotenv()

documents = []

knowledge_folder = "../knowledge"

for file in os.listdir(knowledge_folder):

    if file.endswith(".txt"):

        loader = TextLoader(
            os.path.join(knowledge_folder, file),
            encoding="utf-8"
        )

        documents.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

db = FAISS.from_documents(
    docs,
    embeddings
)

db.save_local("../vector_db")

print("Vector database created successfully!")