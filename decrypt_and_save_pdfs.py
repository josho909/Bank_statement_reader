import os
import fitz

# Function to decrypt and resave PDF's
def decrypt_and_save_pdfs(input_folder, pdf_folder, password):
    try:
        # Ensure the output folder exists
        os.makedirs(pdf_folder, exist_ok=True)
        
        # Iterate through all files in the input folder
        for filename in os.listdir(input_folder):
            if filename.endswith(".pdf"):
                input_pdf_path = os.path.join(input_folder, filename)
                output_pdf_path = os.path.join(pdf_folder, filename)
                
                # Open the PDF file
                pdf_document = fitz.open(input_pdf_path)
                
                # Check if the PDF is encrypted
                if pdf_document.is_encrypted:
                    # Try to authenticate using the provided password
                    if pdf_document.authenticate(password):
                        # If authentication is successful, save a copy of the PDF without encryption
                        pdf_document.save(output_pdf_path)
                        
                        # Close the PDF file
                        pdf_document.close()
                        
                        print(f"PDF '{filename}' decrypted successfully. Decrypted PDF saved to '{output_pdf_path}'.")
                    else:
                        print(f"PDF '{filename}': Incorrect password. Unable to decrypt.")
                else:
                    # If the PDF is not encrypted, save a copy without encryption
                    pdf_document.save(output_pdf_path)
                    
                    # Close the PDF file
                    pdf_document.close()
                    
                    print(f"PDF '{filename}' is not encrypted. Non-password-protected version saved to '{output_pdf_path}'.")
    
    except Exception as e:
        print(f"Error: {e}")