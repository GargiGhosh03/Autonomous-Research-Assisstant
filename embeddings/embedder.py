import os
import json
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
import chromadb

# === Paths ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "..", "data", "processed_chunks.json")
chroma_path = os.path.join(BASE_DIR, "..", "data", "vector_store")

# ✅ Ensure ChromaDB persistence directory exists
os.makedirs(chroma_path, exist_ok=True)

# === Load chunks from JSON ===
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

chunks = data.get("chunks", [])
if not chunks:
    print("❌ No chunks found in JSON.")
    exit(1)

print(f"✅ Loaded {len(chunks)} chunks from: {json_path}")

# === Load embedding model ===
print("🔄 Loading SentenceTransformer model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# === Initialize ChromaDB (NEW CLIENT) ===
print(f"🔗 Initializing ChromaDB at: {chroma_path}")
client = chromadb.PersistentClient(path=chroma_path)
collection = client.get_or_create_collection(name="ra_chunks")

# === Embed and store ===
added = 0
for chunk in tqdm(chunks, desc="🔗 Embedding and Storing"):
    try:
        chunk_id = chunk["id"]
        text = chunk["text"]
        source = chunk.get("source", "unknown")

        if not text.strip():
            continue

        embedding = model.encode(text).tolist()

        collection.add(
            documents=[text],
            embeddings=[embedding],
            metadatas=[{"chunk_id": chunk_id, "source": source}],
            ids=[chunk_id]
        )

        added += 1

    except Exception as e:
        print(f"❌ Error embedding chunk {chunk.get('id', 'unknown')} → {e}")

# === Completion ===
print(f"\n✅ Done. Total chunks embedded and stored: {added}")
print(f"📦 Vector store persisted at: {chroma_path}")
