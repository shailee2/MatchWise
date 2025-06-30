# app.py
import streamlit as st
from resume_parser import extract_text_from_pdf, extract_text_from_txt
from matcher import compute_similarity, find_missing_keywords

st.title("📄 RecruitRater – Resume & Job Description Matcher")

# Upload Resume
st.subheader("1. Upload Your Resume")
resume_file = st.file_uploader("Upload PDF or TXT file", type=['pdf', 'txt'])

# Job Description Input
st.subheader("2. Paste the Job Description")
job_description = st.text_area("Paste the job description here")

# Process Inputs and Show Results
if resume_file and job_description:
    if resume_file.name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(resume_file)
    else:
        resume_text = extract_text_from_txt(resume_file)

    st.subheader("3. Match Results")

    similarity = compute_similarity(resume_text, job_description)
    st.metric("Resume-Job Match Score", f"{similarity}%")

    missing = find_missing_keywords(resume_text, job_description)
    if missing:
        st.warning("🛑 Missing Keywords:")
        for kw in missing:
            st.write(f"- {kw}")
    else:
        st.success("✅ All major keywords are covered!")
