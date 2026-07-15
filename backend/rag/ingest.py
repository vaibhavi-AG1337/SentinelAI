import os

from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from rag.embeddings import get_embeddings
from rag.loader import load_documents

load_dotenv()


def build_vector_database():

    print("Loading cybersecurity documents...")

    documents = load_documents()

    print(f"Loaded {len(documents)} documents.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    embeddings = get_embeddings()

    print("Generating embeddings...")

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    save_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "vector_db"
    )

    vector_store.save_local(save_path)

    print("✅ Vector Database Created Successfully!")


if __name__ == "__main__":
    build_vector_database()