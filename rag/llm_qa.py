import os
from sentence_transformers import SentenceTransformer
import chromadb
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# === Paths ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
chroma_path = os.path.join(BASE_DIR, "..", "data", "vector_store")

# === Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# === Load ChromaDB
client = chromadb.PersistentClient(path=chroma_path)
collection = client.get_or_create_collection(name="ra_chunks")

# === Load local LLM
print("🔄 Loading local model...")
llm = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.1",
    tokenizer="mistralai/Mistral-7B-Instruct-v0.1",
    device_map="auto",
    max_new_tokens=512
)

# === Retrieve chunks
def retrieve_top_chunks(query, top_k=5):
    embedding = embedding_model.encode(query).tolist()
    results = collection.query(query_embeddings=[embedding], n_results=top_k)

    return [doc for doc in results["documents"][0]]

# === Build prompt
def build_prompt(query, context_chunks):
    context = "\n\n".join(context_chunks)
    return (
        f"You are a helpful research assistant.\n"
        f"Use the following document chunks to answer:\n\n"
        f"{context}\n\n"
        f"Question: {query}\nAnswer:"
    )

# === Ask LLM
def ask_llm(query, top_k=5):
    chunks = retrieve_top_chunks(query, top_k)
    prompt = build_prompt(query, chunks)
    response = llm(prompt)[0]["generated_text"]
    return response.strip().split("Answer:")[-1].strip()

# === CLI
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("question", type=str)
    parser.add_argument("--top_k", type=int, default=5)
    args = parser.parse_args()

    print("\n🧠 Answer:")
    print(ask_llm(args.question, top_k=args.top_k))
