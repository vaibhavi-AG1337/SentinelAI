import os

from langchain_community.vectorstores import FAISS

from rag.embeddings import get_embeddings


def retrieve_context(query: str):

    vector_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "vector_db"
    )

    embeddings = get_embeddings()

    db = FAISS.load_local(
        vector_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(query, k=3)

    context = ""

    sources = []

    for doc in docs:
        context += doc.page_content + "\n\n"

        if "source" in doc.metadata:
            sources.append(os.path.basename(doc.metadata["source"]))

    return context, sources