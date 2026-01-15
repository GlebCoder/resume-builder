import streamlit as st
import re
from services.pdf_parser import extract_text_from_pdf
from services.ai_handler import analyze_resume, generate_improved_resume

# Application Page Configuration
st.set_page_config(page_title="AI Resume Optimizer", page_icon="🚀")

st.title("🚀 AI Resume Analyzer & Optimizer")
st.subheader("Match your experience with your dream job")

# Sidebar for file upload
st.sidebar.header("Upload Details")
st.sidebar.success("✅ API Key is Active")
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
            
            if "429" in report or "RESOURCE_EXHAUSTED" in report:
                st.error("🚦 **Rate Limit Reached.** Google's API is taking a breather. Please wait about 30-60 seconds and try again.")
            elif "Error" in report:
                st.error(f"❌ An error occurred: {report}")
            else:
                # Extract score using regex (e.g., Score: 85%)
                score_match = re.search(r"Score:\s*(\d+)%", report)
                if score_match:
                    score = int(score_match.group(1))
                    st.metric("Overall Match Score", f"{score}%")
                    st.progress(score / 100)
                
                st.markdown("### 📊 Detailed Analysis")
                st.info(report)
    else:
        st.warning("Please upload a PDF and paste a JD.")

if generate_btn:
    if uploaded_file and job_description:
        with st.spinner("Rewriting your resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            new_resume = generate_improved_resume(resume_text, job_description)
            
            if "429" in new_resume or "RESOURCE_EXHAUSTED" in new_resume:
                st.error("🚦 **Rate Limit Reached.** Generating a full resume uses many tokens. Please wait a minute and try again.")
            elif "Error" in new_resume:
                st.error(f"❌ An error occurred: {new_resume}")
            else:
                st.subheader("✨ Your Optimized Resume")
                st.code(new_resume, language="markdown")
                st.download_button(
                    label="📥 Download Optimized Resume (TXT)",
                    data=new_resume,
                    file_name="optimized_resume.txt",
                    mime="text/plain"
                )
    else:
        st.warning("Please upload a PDF and paste a JD.")