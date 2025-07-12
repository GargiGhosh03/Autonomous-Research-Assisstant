import os
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# === Setup paths ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
chroma_path = os.path.join(BASE_DIR, "vector_store")

# Load model and ChromaDB
model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client(Settings(persist_directory=chroma_path))
collection = client.get_or_create_collection(name="ra_chunks")

# === Start Query Loop ===
print("\n🧠 Ask me a research question (type 'exit' to quit):")

while True:
    query = input("🔍 Query: ").strip()
    if not query or query.lower() in {"exit", "quit"}:
        print("👋 Exiting. Goodbye!")
        break

    try:
        # Embed query
        query_embedding = model.encode(query).tolist()

        # Search ChromaDB
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=5,
            include=["documents", "metadatas"]
        )

        docs = results["documents"][0]
        metas = results["metadatas"][0]

        print("\n🔎 Top Matches:")
        for i, (doc, meta) in enumerate(zip(docs, metas)):
            print(f"\n#{i + 1}")
            print(f"📄 Source: {meta.get('source', 'Unknown')}")
            print(f"📄 Page: {meta.get('page_number', 'N/A')}")
            print(f"📝 Chunk:\n{doc.strip()[:1000]}")  # limit long chunks
        print("\n" + "-" * 60)

    except Exception as e:
        print(f"❌ Error while searching: {e}")
