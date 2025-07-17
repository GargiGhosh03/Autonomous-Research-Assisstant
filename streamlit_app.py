import os
import streamlit as st
import chromadb
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# === Paths ===
CHROMA_PATH = os.path.join("data", "vector_store")

# === Load embeddings model ===
@st.cache_resource
def load_embedder():
    return SentenceTransformer("all-MiniLM-L6-v2")

# === Load LLM pipeline (lightweight) ===
@st.cache_resource
def load_qa_pipeline():
    return pipeline("text-generation", model="distilgpt2")

# === Load vector store ===
@st.cache_resource
def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    return client.get_or_create_collection(name="ra_chunks")

# === Search ChromaDB ===
def retrieve_chunks(query, embedder, collection, top_k):
    query_embedding = embedder.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return results["documents"][0]

# === Prompt Builder ===
def build_prompt(context, question):
    return f"Context: {context}\n\nQuestion: {question}\nAnswer:"

# === Streamlit UI ===
st.set_page_config(page_title="RA", layout="centered")
st.title("📄 Research Assistant ")

embedder = load_embedder()
qa_pipeline = load_qa_pipeline()
collection = get_collection()

top_k = st.sidebar.slider("Top chunks", 1, 10, 3)
query = st.text_input("Ask a question based on your PDFs:")

if st.button("Ask") and query.strip():
    with st.spinner("Thinking..."):
        docs = retrieve_chunks(query, embedder, collection, top_k)
        context = "\n\n".join(docs)
        prompt = build_prompt(context, query)
        response = qa_pipeline(prompt, max_new_tokens=100)[0]['generated_text']
        answer = response.split("Answer:")[-1].strip()

    st.subheader("🧠 Answer")
    st.write(answer)

    with st.expander("🔍 Chunks used"):
        for i, chunk in enumerate(docs):
            st.markdown(f"**Chunk {i+1}:**\n```\n{chunk[:400]}\n```")
else:
    st.info("Enter a question and click 'Ask'.")

