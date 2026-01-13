import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the SDK
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def analyze_resume(resume_text, job_description):
    """
    Sends resume and JD to Gemini using the stable google-generativeai SDK.
    """
    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        prompt = f"""
        You are an expert HR Manager. 
        Analyze this Resume against the Job Description.
        
        Resume: {resume_text}
        JD: {job_description}
        
        Return:
        1. Match Score (%)
        2. Missing Keywords
        3. Top 3 Improvements
        """
        
        # Generate content
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"AI Analysis Error: {str(e)}"