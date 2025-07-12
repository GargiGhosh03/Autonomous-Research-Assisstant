import os
from utils.pdf_parser import create_json_from_pdfs 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pdf_dir = os.path.join(BASE_DIR, "data", "raw_pdfs")
output_path = os.path.join(BASE_DIR, "data", "processed_chunks.json")

print("Looking for PDFs in:", pdf_dir)
print("Files found:", os.listdir(pdf_dir))

create_json_from_pdfs(pdf_dir, output_path)
