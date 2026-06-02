import fitz 

def extract_text_from_pdf(pdf_path):
    """
    Extract text from PDF resume file.
    
    Args:
        pdf_path(str) : Path to the PDF file.
        
    Returns:
        str: Extracted text
    """

    text = ""

    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)

        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)

            text += page.get_text() + "\n"

        pdf_document.close()

        return text.strip()
    
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""
    

    def is_resume_empty(text):
        """
        Check if the extracted resume text is empty or not.
        
        Args:
            text(str) : Extracted text from the resume.

        Returns:
            bool: True if the resume is empty, False otherwise.
        """

        return len(text.strip()) == 0