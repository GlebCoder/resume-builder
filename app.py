import streamlit as st
import re
import time
from services.pdf_parser import extract_text_from_pdf
from services.ai_handler import analyze_resume, generate_improved_resume, generate_cover_letter
from services.pdf_generator import create_pdf

# Application Page Configuration
st.set_page_config(page_title="AI Resume Optimizer", page_icon="🚀")

st.title("🚀 AI Resume Analyzer & Optimizer")
st.subheader("Match your experience with your dream job")

# Sidebar for file upload and status
st.sidebar.header("Upload Details")
st.sidebar.success("✅ API Key is Active")
uploaded_file = st.sidebar.file_uploader("Upload your Resume (PDF)", type=["pdf"])

# Main area for Job Description input
job_description = st.text_area("Paste the Job Description here:", height=300)

# Main logic execution
if st.button("🚀 Process My Application", use_container_width=True):
    if uploaded_file and job_description:
        with st.spinner("Magic in progress..."):
            # Step 1: Extract text from the uploaded PDF
            resume_text = extract_text_from_pdf(uploaded_file)
            
            # Step 2: Run Analysis first to check for API availability
            report = analyze_resume(resume_text, job_description)
            
            # Step 3: Centralized Error Handling for Rate Limits (429)
            if "429" in report or "RESOURCE_EXHAUSTED" in report:
                st.warning("🚦 Rate Limit Reached. Google's AI needs a short break.")
                
                # Visual countdown for the user
                countdown_placeholder = st.empty()
                progress_bar = st.progress(0)
                
                for seconds_left in range(30, 0, -1):
                    countdown_placeholder.write(f"Refilling API tokens... Please wait {seconds_left}s")
                    progress_bar.progress((30 - seconds_left + 1) / 30)
                    time.sleep(1)
                
                countdown_placeholder.empty()
                st.info("🔄 API is refreshed! You can now click the button again.")
                
            else:
                # Step 4: If no error, proceed to generate Resume and Cover Letter
                # We use Tabs to keep the UI clean and organized
                tab1, tab2, tab3 = st.tabs(["📊 Analysis", "✨ New Resume", "✉️ Cover Letter"])
                
                # --- TAB 1: Detailed Analysis & Match Score ---
                with tab1:
                    score_match = re.search(r"Score:\s*(\d+)%", report)
                    if score_match:
                        score_val = int(score_match.group(1))
                        st.metric("Overall Match Score", f"{score_val}%")
                        st.progress(score_val / 100)
                    
                    st.markdown("### HR Analysis Report")
                    st.markdown(report)
                
                # --- TAB 2: Optimized Resume Generation ---
                with tab2:
                    new_resume = generate_improved_resume(resume_text, job_description)
                    st.subheader("Optimized Content")
                    st.code(new_resume, language="markdown")
                    
                    # PDF Export for Resume
                    resume_pdf = create_pdf(new_resume)
                    st.download_button(
                        label="📥 Download Optimized Resume (PDF)",
                        data=bytes(resume_pdf),
                        file_name="optimized_resume.pdf",
                        mime="application/pdf"
                    )
                
                # --- TAB 3: Cover Letter Generation ---
                with tab3:
                    letter = generate_cover_letter(resume_text, job_description)
                    st.subheader("Tailored Cover Letter")
                    st.write(letter)
                    
                    # PDF Export for Cover Letter
                    letter_pdf = create_pdf(letter)
                    st.download_button(
                        label="📥 Download Cover Letter (PDF)",
                        data=bytes(letter_pdf),
                        file_name="cover_letter.pdf",
                        mime="application/pdf"
                    )
    else:
        # Prompt user if inputs are missing
        st.warning("Please upload a resume and provide a job description to begin.")

# End of app.py logic