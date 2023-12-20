<!-- 
Statement Reader Code
Author - Josh Overett
This program is designed to extract transaction data from monthly PDF bank statements.
The first program pdf_decrypter.py takes three arguments:
    1. It opens each PDF in the first folder
    2. Resaves it in the second folder
    3. After applying the password given in the third argument 
    
The second program statement_reader.py runs by calling the function convert_pdfs_to_table which takes three arguments.

The convert_pdfs_to_table functions arguments are:
    1. Input folder
    2. Output folder
    3. Table names 
A for loop is used to itterate through the three table names within each monthly PDF.
    1. Offset
    2. Fixed
    3. Variable 
    
The result is three csv files saved to the output folder containing all the relevant transactions within the monthly PDF statements 
-->