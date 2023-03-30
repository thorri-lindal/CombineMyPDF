import os
import fitz

# set the directory path
directory = os.getcwd()

# create a list of all pdf files in the directory
pdf_files = [file for file in os.listdir(directory) if file.endswith('.pdf')]

# sort the list of pdf files alphabetically
pdf_files.sort()

# create a PDF document
pdf_doc = fitz.open()

# loop through the list of pdf files and append them to the document
for pdf_file in pdf_files:
    pdf_path = os.path.join(directory, pdf_file)
    pdf_bytes = open(pdf_path, 'rb').read()
    pdf = fitz.open('pdf', pdf_bytes)
    pdf_doc.insert_pdf(pdf)

# save the merged document
pdf_doc.save('merged.pdf')

# close the PDF document
pdf_doc.close()

