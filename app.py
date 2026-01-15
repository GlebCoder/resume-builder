import streamlit as st
from services.pdf_parser import extract_text_from_pdf
from services.ai_handler import analyze_resume, generate_improved_resume

# Application Page Configuration
st.set_page_config(page_title="AI Resume Optimizer", page_icon="🚀")

st.title("🚀 AI Resume Analyzer & Optimizer")
st.subheader("Match your experience with your dream job")

# Sidebar for file upload
st.sidebar.header("Upload Details")
uploaded_file = st.sidebar.file_uploader("Upload your Resume (PDF)", type=["pdf"])

# Main area for Job Description
job_description = st.text_area("Paste the Job Description here:", height=300)

# Create two columns for buttons
col1, col2 = st.columns(2)

with col1:
    analyze_btn = st.button("Analyze Match")
with col2:
    generate_btn = st.button("Generate New Resume")

if analyze_btn:
    if uploaded_file and job_description:
        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            report = analyze_resume(resume_text, job_description)
            st.markdown("### 📊 Analysis Report")
            st.info(report)
    else:
        st.warning("Please upload a PDF and paste a JD.")

if generate_btn:
    if uploaded_file and job_description:
        with st.spinner("Rewriting your resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            new_resume = generate_improved_resume(resume_text, job_description)
            st.markdown("### ✨ Optimized Resume Content")
            st.text_area("Copy your new resume from here:", value=new_resume, height=500)
            st.download_button("Download as Text", new_resume, file_name="improved_resume.txt")
    else:
        st.warning("Please upload a PDF and paste a JD.")