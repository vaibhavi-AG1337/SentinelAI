from retriever import get_retriever

retriever = get_retriever()

query = "Someone asked me to share my OTP."

results = retriever.invoke(query)

print(f"Found {len(results)} documents.\n")

for i, doc in enumerate(results, start=1):
    print("=" * 50)
    print(f"Document {i}")
    print("=" * 50)
    print(doc.page_content)
    print()