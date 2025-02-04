import os
import shutil
from PyPDF3 import PdfFileReader

# Create a directory to move non-valid PDFs to
if not os.path.exists("not_valid"):
    os.makedirs("not_valid")

# Loop through all PDFs in the current directory
for file_name in os.listdir("."):
    if file_name.endswith(".pdf"):
        # Open the PDF and check if it's valid
        with open(file_name, "rb") as pdf_file:
            try:
                pdf_reader = PdfFileReader(pdf_file)
                if pdf_reader.isEncrypted:
                    raise Exception("Encrypted PDF")
                if pdf_reader.getNumPages() == 0:
                    raise Exception("Empty PDF")
            except Exception as e:
                print(f"{file_name} is not a valid PDF: {str(e)}")
                # Move the non-valid PDF to the "not_valid" directory
                shutil.move(file_name, "not_valid")

