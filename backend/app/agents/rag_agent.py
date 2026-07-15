from rag.retriever import retrieve_context

def analyze(message):

    _, sources = retrieve_context(message)

    return sources