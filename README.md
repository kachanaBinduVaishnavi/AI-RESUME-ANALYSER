# 📄 AI Resume Analyzer

A web application that analyzes a resume against a job description and identifies matching and missing skills.

## 📌 Project Overview

The AI Resume Analyzer helps job seekers understand how well their resume matches a particular job description.

The application extracts text from an uploaded resume, identifies predefined technical skills, compares them with the job requirements, and displays matching skills, missing skills, and a match score.

## ✨ Features

- Upload a resume in PDF or DOCX format
- Extract text from the resume
- Compare resume skills with job requirements
- Identify matching skills
- Identify missing skills
- Display a resume match score
- Check important resume sections
- Provide basic resume suggestions
- Simple and user-friendly interface

## 🛠️ Technologies Used

- Python
- Streamlit
- HTML
- SQL
- Resume text extraction
- Git & GitHub

## 📂 Project Structure

```text
AI-RESUME-ANALYSER/
│
├── utils/
│   ├── __init__.py
│   └── resume_parser.py
│
├── screenshots/
│   └── Screenshot 2026-09-29 173104.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 📸 Application Screenshot

![AI Resume Analyzer](screenshots/Screenshot%202026-09-29%20173104.png)

## ▶️ Run the Application

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The application will open in your web browser.

## 📊 How It Works

1. Upload a resume.
2. The application extracts the resume text.
3. Paste a job description.
4. The application identifies predefined skills in the resume and job description.
5. Matching skills and missing skills are displayed.
6. A match percentage is calculated.
7. The application checks important resume sections and provides suggestions.

## 🔮 Future Improvements

- Improve skill extraction using NLP
- Support more resume formats
- Improve skill matching accuracy
- Add advanced resume scoring
- Add job-role recommendations
- Add user authentication
- Deploy the application online

