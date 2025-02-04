import os
import fitz

def combine_pdfs(output_filename='merged.pdf'):
    # Set the directory path
    directory = os.getcwd()

    # Create a list of all PDF files in the directory
    pdf_files = [file for file in os.listdir(directory) if file.endswith('.pdf')]

    # Sort the list of PDF files alphabetically
    pdf_files.sort()

    # Create a PDF document
    pdf_doc = fitz.open()

    # Loop through the list of PDF files and append them to the document
    for pdf_file in pdf_files:
        # Construct the full file path
        pdf_path = os.path.join(directory, pdf_file)
        try:
            # Open the PDF file in binary read mode
            with open(pdf_path, 'rb') as f:
                # Read the content of the file
                pdf_bytes = f.read()
            # Open the PDF from the bytes read
            pdf = fitz.open('pdf', pdf_bytes)
            # Insert the PDF into the main document
            pdf_doc.insert_pdf(pdf)
            # Print a message indicating the file was added
            print(f"Added {pdf_file}")
        except Exception as e:
            # Print an error message if there is an issue adding the file
            print(f"Error adding {pdf_file}: {e}")

    # Save the merged document
    try:
        pdf_doc.save(output_filename)
        print(f"Merged PDF saved as {output_filename}")
    except Exception as e:
        print(f"Error saving merged PDF: {e}")

    # Close the PDF document
    pdf_doc.close()

if __name__ == "__main__":
    combine_pdfs()

