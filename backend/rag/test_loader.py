from loader import load_documents

docs = load_documents()

print(f"Loaded {len(docs)} documents.\n")

for doc in docs:
    print("=" * 40)
    print(doc.page_content)