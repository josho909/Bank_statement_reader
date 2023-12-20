import decrypt_and_save_pdfs

# Initialise parameters
password = "19011981JOS"
input_folder = "C:/Users/josho/Dropbox/Misc/Laura Street/PDF"
pdf_folder = "C:/Users/josho/Dropbox/Misc/Laura Street/PDF_decrypted"

# Decrypt and save PDFs in the specified folder
decrypt_and_save_pdfs.decrypt_and_save_pdfs(input_folder, pdf_folder, password)