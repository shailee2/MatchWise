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

MatchWise/ <br>
│ <br>
├── backend/ <br>
│ ├── app.py # Flask backend with REST endpoints <br>
│ ├── resume_matcher.py # NLP and scoring logic <br>
│ ├── parser.py # PDF extraction utilities <br>
│ └── requirements.txt <br>
│ <br>
├── frontend/ <br>
│ ├── src/ <br>
│ ├── public/ <br>
│ └── package.json <br>
│ <br>
├── README.md <br>
└── .gitignore <br>


## Use Cases

- Career centers and universities screening student resumes
- Job seekers optimizing their resumes for specific roles
- Recruiters doing preliminary fit checks

## Setup Instructions

1. **Backend Setup**
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
    ```
2. **Frontend Setup**
```bash
cd frontend
npm install
npm start
```
