# matcher.py
from sentence_transformers import SentenceTransformer, util
import spacy

# Load the model only once when this file is imported
model = SentenceTransformer('all-MiniLM-L6-v2')
nlp = spacy.load("en_core_web_sm")

def compute_similarity(resume_text, job_text):
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    job_embedding = model.encode(job_text, convert_to_tensor=True)
    similarity = util.cos_sim(resume_embedding, job_embedding)
    return round(float(similarity[0][0]) * 100, 2)  # convert tensor to float percentage

def extract_keywords(text, top_n=10):
    doc = nlp(text)
    # Use noun chunks to get important phrases (e.g., "data analysis", "Python programming")
    return list(set([chunk.text.lower() for chunk in doc.noun_chunks if len(chunk.text) > 3]))[:top_n]

def find_missing_keywords(resume_text, job_text):
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_text)
    missing = [kw for kw in job_keywords if kw not in resume_keywords]
    return missing
