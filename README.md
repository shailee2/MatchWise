# MatchWise

**MatchWise** is an AI-powered resume-job matching tool that uses NLP and semantic analysis to evaluate how well a resume aligns with a given job description. It’s designed for students, recruiters, and job seekers to quickly assess fit and optimize their applications.

## Features

- Uploads and parses PDF resumes and job descriptions
- Uses sentence embeddings and NLP techniques to compare content
- Highlights matched skills, experience, and role-specific keywords
- Displays a similarity score and visual breakdown of strengths/gaps
- User-friendly web interface for uploading and viewing results

## Tech Stack

- **Frontend:** React.js, TailwindCSS  
- **Backend:** Flask, Python  
- **NLP:** spaCy, sentence-transformers, PDFMiner  
- **AI:** Pretrained transformer models for sentence similarity  
- **Others:** RESTful API, Git, GitHub

## How It Works

1. Upload a resume and a job description (PDFs).
2. The backend extracts and processes text using PDFMiner and spaCy.
3. Sentence embeddings are generated and compared for semantic overlap.
4. A similarity score is computed using cosine similarity.
5. Results are sent back to the frontend for display and interpretation.

## Project Structure
