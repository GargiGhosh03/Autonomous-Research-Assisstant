# 🧠 Autonomous Research Assistant (RA)

A fully local, AI-powered research assistant built using PDF parsing, chunking, semantic embedding with `sentence-transformers`, and vector search using `ChromaDB`. Designed to help researchers extract, search, and interact with large volumes of academic literature — with a **Streamlit interface** for natural question-answering.

---

## 🚀 Features

- ✅ Parse and extract content from academic PDFs
- ✅ Intelligent chunking using `unstructured`
- ✅ Embedding using `all-MiniLM-L6-v2`
- ✅ Fast semantic search via ChromaDB
- ✅ Streamlit-based Q&A interface
- ✅ 100% local (no cloud dependencies)
- ✅ Modular design for easy extension

---

## 🗂️ Folder Structure

Autonomous-RA/
├── data/

│ └── raw_pdfs/ # Your uploaded academic papers

│ └── processed_chunks.json # Cleaned and chunked text with metadata

├── embeddings/

│ └── embedder.py # Embeds all chunks into ChromaDB

├── vector_store/ # ChromaDB persistent vector index

├── utils/

│ └── pdf_parser.py # PDF parsing and chunk extraction logic

├── streamlit_app.py # Frontend UI for querying the assistant

├── requirements.txt

└── README.md


## 🛠️ Installation

## Clone the repo
git clone https://github.com/yourusername/Autonomous-RA.git
cd Autonomous-RA

## Install dependencies
pip install -r requirements.txt
 
