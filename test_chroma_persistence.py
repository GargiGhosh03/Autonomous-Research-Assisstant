import os
import chromadb
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
chroma_path = os.path.join(BASE_DIR, "data", "vector_store_test")

# Create directory
os.makedirs(chroma_path, exist_ok=True)

# ✅ New Chroma client
client = chromadb.PersistentClient(path=chroma_path)
collection = client.get_or_create_collection(name="test_collection")

# Embed a test doc
model = SentenceTransformer("all-MiniLM-L6-v2")
text = "This is a test document."
embedding = model.encode(text).tolist()

collection.add(
    documents=[text],
    embeddings=[embedding],
    metadatas=[{"tag": "test"}],
    ids=["test_001"]
)

print("✅ Stored test embedding.")
print("📁 Vector store contents:", os.listdir(chroma_path))