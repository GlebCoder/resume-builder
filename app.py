import streamlit as st
from services.pdf_parser import extract_text_from_pdf
from services.ai_handler import analyze_resume

# Application Page Configuration
st.set_page_config(page_title="AI Resume Optimizer", page_icon="🚀")

st.title("🚀 AI Resume Analyzer & Optimizer")
st.subheader("Match your experience with your dream job")

# Sidebar for file upload
st.sidebar.header("Upload Details")
uploaded_file = st.sidebar.file_uploader("Upload your Resume (PDF)", type=["pdf"])

# Main area for Job Description
job_description = st.text_area("Paste the Job Description here:", height=300)

if st.button("Analyze Resume"):
    if uploaded_file and job_description:
        with st.spinner("Analyzing... Please wait."):
            # 1. Extract text from PDF
            resume_text = extract_text_from_pdf(uploaded_file)
            
            # 2. Call AI Handler
            analysis_result = analyze_resume(resume_text, job_description)
            
            # 3. Display Result
            st.success("Analysis Complete!")
            st.markdown("### AI Analysis Report")
            st.write(analysis_result)
    else:
        st.error("Please upload a resume and paste a job description.")