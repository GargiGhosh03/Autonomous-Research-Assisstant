import os
import chromadb
from sentence_transformers import SentenceTransformer
import sys
if len(sys.argv) == 1:
    sys.argv += ["What is machine learning?"]
    
# === Paths ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
chroma_path = os.path.join(BASE_DIR, "..", "data", "vector_store")

# === Load embedding model manually
model = SentenceTransformer("all-MiniLM-L6-v2")

# === Initialize Chroma without embedding function
client = chromadb.PersistentClient(path=chroma_path)
collection = client.get_or_create_collection(name="ra_chunks")

# === Manual embedding search function
def search_chunks(query, top_k=5):
    embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[embedding], n_results=top_k)

    docs = results["documents"][0]
    metadatas = results["metadatas"][0]
    ids = results["ids"][0]

    print(f"\n🔎 Top {top_k} results for query: \"{query}\"")
    for i in range(len(docs)):
        print(f"\n[{i+1}] 📄 Source: {metadatas[i]['source']} | Chunk ID: {metadatas[i]['chunk_id']}")
        print(f"→ {docs[i][:300]}{'...' if len(docs[i]) > 300 else ''}")  # preview

# === CLI runner
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="Search query")
    parser.add_argument("--top_k", type=int, default=5, help="Top K results")
    args = parser.parse_args()

    search_chunks(args.query, top_k=args.top_k)