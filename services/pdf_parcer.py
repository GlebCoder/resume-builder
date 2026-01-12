from pypdf import PdfReader

def extract_text_from_pdf(pdf_file):
    """
    Извлекает текст из загруженного PDF-файла.
    """
    try:
        reader = PdfReader(pdf_file)
        full_text = ""
        
        for page in reader.pages:
            # Извлекаем текст из каждой страницы и добавляем перенос
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + "\n"
        
        return full_text.strip()
    
    except Exception as e:
        return f"Ошибка при чтении PDF: {str(e)}"