import os
from google import genai  # Ensure this matches the google-genai library
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def analyze_resume(resume_text, job_description):
    """
    Analyzes the resume against the job description.
    """
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    
    prompt = f"""
    You are an expert HR Manager. 
    Analyze this Resume against the Job Description.
    
    IMPORTANT: Start your response with "Score: [number]%" 
    
    Resume: {resume_text}
    JD: {job_description}
    # ... rest of the prompt
    
    Resume: {resume_text}
    JD: {job_description}
    
    Return:
    1. Match Score (%)
    2. Missing Keywords
    3. Top 3 Improvements
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI Analysis Error: {str(e)}"

def generate_improved_resume(resume_text, job_description):
    """
    Generates an optimized version of the resume.
    """
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    
    prompt = f"""
    You are a professional Resume Writer. 
    Rewrite the following Resume to perfectly match the Job Description.
    
    INSTRUCTIONS:
    - Keep the information true to the original.
    - Enhance descriptions using action verbs and metrics.
    - Integrate missing keywords.
    - Use a professional, clean format.
    
    ---
    JOB DESCRIPTION:
    {job_description}
    
    ---
    ORIGINAL RESUME:
    {resume_text}
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error during generation: {str(e)}"
    
def generate_cover_letter(resume_text, job_description):
    """
    Generates a professional cover letter based on resume and job description.
    """
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    
    prompt = f"""
    You are a professional Career Coach. Write a compelling Cover Letter 
    that connects the candidate's experience to the specific needs of the job.
    
    INSTRUCTIONS:
    - Focus on how the candidate's skills solve the company's problems.
    - Use a professional yet enthusiastic tone.
    - Keep it concise (3-4 paragraphs).
    - Use placeholders like [Hiring Manager Name] where appropriate.
    
    ---
    CANDIDATE RESUME:
    {resume_text}
    
    ---
    JOB DESCRIPTION:
    {job_description}
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Cover Letter Error: {str(e)}"