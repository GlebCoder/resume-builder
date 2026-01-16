from fpdf import FPDF

def create_pdf(text, filename="output.pdf"):
    pdf = FPDF()
    pdf.add_page()
    
    # Set safe margins
    pdf.set_margins(15, 15, 15)
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Pre-clean the text
    clean_text = text.replace("–", "-").replace("—", "-").replace("**", "").replace("* ", "- ")
    
    lines = clean_text.split('\n')
    
    for line in lines:
        stripped_line = line.strip()
        
        # 1. Skip empty lines
        if not stripped_line:
            pdf.ln(4)
            continue
            
        # 2. Detect Section Headers (e.g., # EXPERIENCE or EDUCATION)
        if line.startswith('#') or (line.isupper() and len(stripped_line) > 3):
            pdf.set_font("Arial", style="B", size=14)
            header_text = line.lstrip('#').strip()
            pdf.multi_cell(0, 10, txt=header_text)
            pdf.ln(1)
            
        # 3. Detect Company Names / Job Titles
        # Matches lines like "Company: Google" or "Uber | Senior Manager"
        elif "Company:" in line or " | " in line or "Employer:" in line:
            pdf.set_font("Arial", style="B", size=11)
            pdf.multi_cell(0, 8, txt=stripped_line)
            
        # 4. Regular Text (Bullet points, descriptions)
        else:
            pdf.set_font("Arial", size=11)
            try:
                # Use a smaller line height for body text to keep it compact
                pdf.multi_cell(0, 7, txt=stripped_line)
            except Exception:
                pdf.write(7, stripped_line)
                pdf.ln(7)
            
    return pdf.output()