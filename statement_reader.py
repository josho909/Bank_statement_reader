for account_type, table_position in account_table.iterrows():
    convert_pdfs_to_table(pdf_folder, output_folder, account_type)
    print(f'account is storing: <{account_type}> table position is storing: <{table_position}>')