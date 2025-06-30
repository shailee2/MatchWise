# resume_parser.py
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_file):
    return extract_text(pdf_file)

def extract_text_from_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8")
