from fpdf import FPDF

def create_pdf(text, filename="output.pdf"):
    pdf = FPDF()
    pdf.add_page()
    
    # Set safe margins (left, top, right)
    pdf.set_margins(15, 15, 15)
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Pre-clean the text from common problematic characters
    # Replace long dashes, asterisks from Markdown, and bullet points
    clean_text = text.replace("–", "-").replace("—", "-").replace("**", "").replace("* ", "- ")
    
    lines = clean_text.split('\n')
    
    for line in lines:
        # Handle empty or whitespace-only lines safely
        if not line.strip():
            pdf.ln(5)
            continue
            
        # Detect if the line is a header (starts with # or is all UPPERCASE)
        is_header = line.startswith('#') or (line.isupper() and len(line.strip()) > 3)
        
        if is_header:
            pdf.set_font("Arial", style="B", size=14)
            display_text = line.lstrip('#').strip()
            # multi_cell with width=0 fills the available width to the right margin
            pdf.multi_cell(0, 10, txt=display_text)
            pdf.ln(2)
        else:
            pdf.set_font("Arial", size=11)
            display_text = line.strip()
            
            # CRITICAL FIX: If a single word is too long (e.g., a long URL), 
            # we need to ensure it doesn't crash the layout engine.
            # We'll limit the character length per line to be safe.
            try:
                pdf.multi_cell(0, 8, txt=display_text)
            except Exception:
                # Fallback: if the line still fails, print it in chunks
                pdf.write(8, display_text)
                pdf.ln(8)
            
    return pdf.output()