from pypdf import PdfReader


def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a provided PDF file object.
    """
    try:
        reader = PdfReader(pdf_file)
        full_text = ""
        
        # Iterate through each page of the PDF
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + "\n"
        
        # Remove leading/trailing whitespace
        return full_text.strip()
    
    except Exception as e:
        # Return error message if parsing fails
        return f"Error reading PDF: {str(e)}"