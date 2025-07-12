import os
import streamlit as st
from sentence_transformers import SentenceTransformer
import chromadb
from transformers import pipeline

# === Config paths ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHROMA_PATH = os.path.join(BASE_DIR, "data", "vector_store")

# === Load models ===
@st.cache_resource
def load_models():
    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    llm = pipeline(
        "text-generation",
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", 
        tokenizer="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        device_map="auto",
        max_new_tokens=512
    )
    return embedding_model, llm

embedding_model, llm = load_models()

# === Load vector store ===
client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_or_create_collection(name="ra_chunks")

# === Helper to retrieve top chunks
def retrieve_chunks(query, top_k=5):
    embedding = embedding_model.encode(query).tolist()
    results = collection.query(query_embeddings=[embedding], n_results=top_k)
    return results["documents"][0]

# === Prompt formatter
def build_prompt(query, chunks):
    context = "\n\n".join(chunks)
    return f"You are a helpful assistant. Use the following context to answer:\n\n{context}\n\nQuestion: {query}\nAnswer:"

# === Streamlit UI ===
st.set_page_config(page_title="Autonomous RA", layout="wide")
st.title("🧠 Autonomous Research Assistant")
st.markdown("Ask questions based on your local PDFs and get LLM-powered answers — no internet required!")

# === Query input
query = st.text_input("Enter your question")

top_k = st.slider("Number of chunks to retrieve", 1, 10, 5)

if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            chunks = retrieve_chunks(query, top_k)
            prompt = build_prompt(query, chunks)
            response = llm(prompt)[0]["generated_text"]
            answer = response.strip().split("Answer:")[-1].strip()

        st.subheader("🧠 Answer")
        st.write(answer)

        with st.expander("📄 Context Used"):
            for i, chunk in enumerate(chunks):
                st.markdown(f"**Chunk {i+1}:** {chunk[:300]}{'...' if len(chunk) > 300 else ''}")
