import streamlit as st
import re
from services.pdf_parser import extract_text_from_pdf
from services.ai_handler import analyze_resume, generate_improved_resume, generate_cover_letter
from services.pdf_generator import create_pdf

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

# 1. Сначала импортируем новую функцию (проверь строку импорта вверху!)
# from services.ai_handler import analyze_resume, generate_improved_resume, generate_cover_letter

# 2. Кнопка запуска общего процесса
if st.button("🚀 Process My Application", use_container_width=True):
    if uploaded_file and job_description:
        with st.spinner("Magic in progress..."):
            # Извлекаем текст один раз для экономии времени
            resume_text = extract_text_from_pdf(uploaded_file)
            
            # Создаем вкладки
            tab1, tab2, tab3 = st.tabs(["📊 Analysis", "✨ New Resume", "✉️ Cover Letter"])
            
            with tab1:
                report = analyze_resume(resume_text, job_description)
                # Красивый вывод Score, как мы делали вчера
                score_match = re.search(r"Score:\s*(\d+)%", report)
                if score_match:
                    score = int(score_match.group(1))
                    st.metric("Match Score", f"{score}%")
                    st.progress(score / 100)
                st.markdown(report)
            
            with tab2:
                new_resume = generate_improved_resume(resume_text, job_description)
                st.code(new_resume, language="markdown")
                
                # PDF Generation
                resume_pdf = create_pdf(new_resume)
                st.download_button(
                    label="📥 Download Resume as PDF",
                    data=bytes(resume_pdf),
                    file_name="improved_resume.py.pdf",
                    mime="application/pdf"
                )
                
            with tab3:
                letter = generate_cover_letter(resume_text, job_description)
                st.markdown("### Generated Cover Letter")
                st.write(letter)
                
                # PDF Generation
                letter_pdf = create_pdf(letter)
                st.download_button(
                    label="📥 Download Letter as PDF",
                    data=bytes(letter_pdf),
                    file_name="cover_letter.pdf",
                    mime="application/pdf"
                )
        st.warning("Please upload your resume and paste the job description first.")