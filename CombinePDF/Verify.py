import os
from PyPDF3 import PdfFileReader

def validate_pdf(file_path):
    """
    Validate a PDF file by trying to open it using PyPDF3.
    Return True if the file is a valid PDF, False otherwise.
    """
    try:
        with open(file_path, 'rb') as f:
            pdf = PdfFileReader(f)
            # Accessing the number of pages of a PDF will ensure the file is valid
            num_pages = pdf.getNumPages()
            return True
    except:
        return False

# Validate all PDF files in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        if validate_pdf(filename):
            print(f'{filename} is a valid PDF')
        else:
            print(f'{filename} is not a valid PDF')

