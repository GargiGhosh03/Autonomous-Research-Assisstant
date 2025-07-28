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

## 🔧 Additional Dependencies (Required for PDF Parsing)

This project uses OCR to extract text from scanned or image-based PDFs. Make sure the following system tools are installed and added to your PATH:

📌 1. Poppler
Poppler is required for reading and converting PDF pages.

Windows: Download from Poppler for Windows.

Extract it `(e.g., C:\poppler)`.

Add the path to `C:\poppler\Library\bin in your system environment variables (PATH)`.

📌 2. Tesseract OCR
Tesseract is used for extracting text from images within PDFs.

Windows: Download the installer from Tesseract GitHub.

Install to a known location `(e.g., C:\Tesseract-OCR)`.

Add that folder to your PATH environment variable.

## 🛠️ Installation
pip install -r requirements.txt

## 🖥 Interface Walkthrough

### 🧪 Interaction Interface

<table>
  <tr>
    <td style="width: 50%; vertical-align: top; padding: 10px;">
      <p>
        Users can write the desired questions they want in the box. The chunks can be adjusted on the desired requirements of the user (max 10) i.e how many extracts they want from different research paper. 
      </p>
    </td>
    <td style="width: 50%; padding: 10px;">
      <img src="https://github.com/user-attachments/assets/b2293920-a66a-4a16-8e9d-77f698b72369" alt="Upload Interface" style="max-width: 100%; border-radius: 10px;" />
    </td>
  </tr>
</table>

### 🧪 Question 

<table>
  <tr>
    <td style="width: 50%; vertical-align: top; padding: 10px;">
      <p>
        Here for e.g "AI" has been written as prompt inside the box to extract the meaningful information or related information which are present inside the research articles/ papers in accordance to AI. The questions can be altered respectively and the desired number of chunks along with the answers can be extracted.  
      </p>
    </td>
    <td style="width: 50%; padding: 10px;">
      <img src="https://github.com/user-attachments/assets/16da1045-5ba4-4e64-9d5d-fc68b9bd9bf7" alt="Upload Interface" style="max-width: 100%; border-radius: 10px;" />
    </td>
  </tr>
