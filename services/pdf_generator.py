from fpdf import FPDF

from fpdf import FPDF

def create_pdf(text, filename="output.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Replace problematic Unicode characters with standard ones
    clean_text = text.replace("–", "-").replace("—", "-")
    clean_text = clean_text.replace('"', '"').replace('"', '"')
    clean_text = clean_text.replace("'", "'").replace("'", "'")
    
    # Latin-1 encode/decode is a trick to strip other hidden weird chars
    clean_text = clean_text.encode('latin-1', 'replace').decode('latin-1')
    
    pdf.multi_cell(0, 10, txt=clean_text)
    return pdf.output()