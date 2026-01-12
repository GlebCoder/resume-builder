# AI Resume Optimizer

An intelligent assistant that helps job seekers tailor their resumes to specific job descriptions. By leveraging Large Language Models, this tool identifies missing keywords, suggests improvements, and ensures your CV is optimized for both Human Recruiters and Applicant Tracking Systems (ATS).

## ✨ Key Features
- **Smart Analysis:** Automatically compares your resume against a job description.
- **Keyword Optimization:** Identifies missing skills and industry-specific terms.
- **Actionable Feedback:** Provides specific suggestions on how to rephrase experience bullet points.
- **PDF Support:** Seamlessly extracts text from existing PDF resumes.

## 🛠 Tech Stack
- **Backend:** Python 3.13
- **AI Logic:** OpenAI GPT-4o API
- **Web UI:** Streamlit
- **PDF Engine:** PyPDF2 / pdfplumber

## 📂 Architecture
The project follows a modular architecture to ensure scalability and ease of maintenance:
- `/core`: Core logic for text analysis and scoring algorithms.
- `/services`: Integration with external APIs (OpenAI) and PDF processing.
- `app.py`: The entry point for the Streamlit web application.

## ⚙️ Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/GlebCoder/resume-builder.git](https://github.com/GlebCoder/resume-builder.git)
   cd resume-builder