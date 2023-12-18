def extract_desc_from_text(text):
    # Define date and number patterns to be stripped to return only transaction descriptions
    date_pattern = re.compile(r'^\d{2} \w{3}')
    number_pattern = re.compile(r'[0-9.,-]')

    # Iterate through lines and remove the date pattern
    stripped_lines = []
    for line in text.split('\n'):
        stripped_line = date_pattern.sub('', line).strip()
        stripped_line = number_pattern.sub('', stripped_line).strip()
        stripped_lines.append(stripped_line)

    return stripped_lines