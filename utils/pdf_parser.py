import os
import json
from unstructured.partition.pdf import partition_pdf
from unstructured.chunking.title import chunk_by_title
from unstructured.documents.elements import CompositeElement

def create_json_from_pdfs(pdf_dir, output_path):
    chunks = []

    for filename in os.listdir(pdf_dir):
        if not filename.lower().endswith(".pdf"):
            continue

        pdf_path = os.path.join(pdf_dir, filename)
        print(f"📄 Parsing: {filename}")

        try:
            # Use hi-res strategy for scanned/image PDFs
            elements = partition_pdf(
                filename=pdf_path,
                strategy="hi_res",  # OCR if needed
                pdf_infer_table_structure=False
            )

            # DEBUG: Print how many elements we got
            print(f"📦 Elements found: {len(elements)}")

            # Optional: filter only structured elements (comment this out if unsure)
            # elements = [el for el in elements if isinstance(el, CompositeElement)]

            chunked_elements = chunk_by_title(elements)

            print(f"🔹 Chunked into: {len(chunked_elements)}")

            for idx, chunk in enumerate(chunked_elements):
                text = chunk.text.strip()
                if not text:
                    continue

                chunk_id = f"{filename}_chunk{idx}"

                chunks.append({
                    "id": chunk_id,
                    "text": text,
                    "source": filename,
                })

        except Exception as e:
            print(f"❌ Failed to process {filename} → {e}")

    # Save to JSON
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"chunks": chunks}, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Saved {len(chunks)} clean chunks to {output_path}")
