import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    """Extract text from each page of a PDF file."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def ingest_documents(raw_dir, processed_dir):
    """Convert all PDFs in raw_dir to .txt files in processed_dir."""
    os.makedirs(processed_dir, exist_ok=True)
    for file in os.listdir(raw_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(raw_dir, file)
            text = extract_text_from_pdf(pdf_path)
            output_path = os.path.join(processed_dir, file.replace(".pdf", ".txt"))
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
    print("✅ Document ingestion complete.")
