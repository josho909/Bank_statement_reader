# Import packages
import pandas as pd
import numpy as np
import PyPDF2
import fitz  # PyMuPDF
import os
import re
import regex
import datetime
import extract_dates_from_text
import extract_desc_from_text
import extract_numbers_from_text

# Function to extract text from each page of PDF's and save to output folder
def convert_pdfs_to_table(pdf_folder, output_folder, saved_filename):
    try:
        # Ensure the output Currency AUD Balancefolder exists
        os.makedirs(output_folder, exist_ok=True)
        
        offset_table_all = pd.DataFrame(
                    {
                        'Date': [],
                        'Description': [],
                        'Balance': []
                    }
                )
        
        # Iterate through all files in the input folder
        for filename in os.listdir(pdf_folder):
            if filename.endswith(".pdf"):
                output_pdf_path = os.path.join(pdf_folder, filename)
                
                # Open the PDF file
                pdf_document = PyPDF2.PdfReader(output_pdf_path)
                
                #print the number of pages
                print(f"{Path(filename).stem} has {len(pdf_document.pages)} pages")
                
                # Re-initialise text and dts list
                text = ''
                dts = []
                
#                 Iterate through pages in PDF and extract the text
                for idx in range(len(pdf_document.pages)):
                    pages = pdf_document.pages[idx]
                    text_new = pages.extract_text()
                    text = text + text_new

#                 Return the second table between Deposits Balance\n and \nTransaction Total
                match = re.findall('(?s)Deposits Balance\n(.*?)\nTransaction Total', text)
                trans = match[table_position[0]]
                for i, row in text_key.iterrows():
                    if str(row[1]) == 'nan':
                        trans = re.sub(str(row[0]), '', trans)
                    elif str(row[1]) == 'Y':
                        trans = re.sub(str(row[0]), '', trans, flags=re.MULTILINE)
                    else:
                        trans = re.sub(str(row[0]), str(row[1]), trans)
                
#                 Get the year from the top of the statement
                year_statement = re.findall('STATEMENT.*\d{2}.{4}( \d{4}?)', text)[0]
                year_statement_num = int(year_statement)
                month_statement = re.findall('STATEMENT.*\d{2} (.{3})', text)[0]
                month_statement_num = datetime.datetime.strptime(month_statement, "%b").month
                
#                 Join the dates, descriptions and balances from the table into a dataframe
                dt = extract_dates_from_text.extract_dates_from_text(trans)
                desc = extract_desc_from_text.extract_desc_from_text(trans)
                bal = extract_numbers_from_text.extract_numbers_from_text(trans)
            
#                 Loop that iterates through the dates and adds the year from the top of the statement
                for idx_dt in dt:
                    day, month = idx_dt.split()

                    # Convert the month to a number
                    month_num = datetime.datetime.strptime(month, "%b").month

                    # Append the year to the date
                    if month_num != 12:
                        idx_dt = f"{idx_dt} {year_statement_num}"
                    elif month_num != month_statement_num:
                        idx_dt = f"{idx_dt} {year_statement_num -1}"
                    else:
                        idx_dt = f"{idx_dt} {year_statement_num}"
                    dt = idx_dt
                    dts.append(dt)

                offset_table = pd.DataFrame(
                    {
                        'Date': dts,
                        'Description': desc,
                        'Balance': bal
                    }
                )
                
                offset_table_all = offset_table_all._append(offset_table, ignore_index=True)
                
#                 Write the offset table to csv files
            file_path = os.path.join(output_folder, f"{saved_filename}_all.csv")

            offset_table_all.to_csv(file_path)
            
        else:
            print(f"PDF transfer to '{file_path}': Complete!")
    
    except Exception as e:
        print(f"Error: {e}\n{trans}")