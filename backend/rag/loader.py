import os
from langchain_community.document_loaders import TextLoader


def load_documents():

    knowledge_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "knowledge"
    )

    documents = []

    for file in os.listdir(knowledge_path):

        if file.endswith(".txt"):

            loader = TextLoader(
                os.path.join(knowledge_path, file),
                encoding="utf-8"
            )

            documents.extend(loader.load())

    return documents