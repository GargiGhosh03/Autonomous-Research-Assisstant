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

##🔧 Additional Dependencies (Required for PDF Parsing)

This project uses OCR to extract text from scanned or image-based PDFs. Make sure the following system tools are installed and added to your PATH:

📌 1. Poppler
Poppler is required for reading and converting PDF pages.

Windows: Download from Poppler for Windows.

Extract it (e.g., C:\poppler).

Add the path to C:\poppler\Library\bin in your system environment variables (PATH).



## 🛠️ Installation
pip install -r requirements.txt
 
