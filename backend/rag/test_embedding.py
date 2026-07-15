from embeddings import get_embeddings

embeddings = get_embeddings()

vector = embeddings.embed_query("This is a phishing email.")

print(len(vector))
print(vector[:10])