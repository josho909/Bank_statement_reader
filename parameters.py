# Import packages
import pandas as pd

# Initialise parameters
password = "19011981JOS"
input_folder = "C:/Users/josho/Dropbox/Misc/Laura Street/PDF"
pdf_folder = "C:/Users/josho/Dropbox/Misc/Laura Street/PDF_decrypted"
txt_output = "C:/Users/josho/Dropbox/Misc/Laura Street/text_output"
output_folder = "C:/Users/josho/Dropbox/Misc/Laura Street/offset_output"
offset_filename = "offset"

# Import text replacement key from csv
text_key = pd.read_csv('C:/Users/josho/Dropbox/Misc/Laura Street/offset_output/text_key.csv', index_col='text_key')

# Create account table and set index
account_table = pd.DataFrame(
                    {
                        'account_name': ['Offset', 'Fixed', 'Variable'],
                        'position_number': [1,2,3]
                    }
                )
account_table = account_table.set_index('account_name')