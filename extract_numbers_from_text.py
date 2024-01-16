import re

def extract_numbers_from_text(text):
    # Define the pattern for matching numbers in the format 12,345.66
    number_pattern = re.compile(r'(?:\d{1,3}[\,])?\d{1,3}[\.]\d{1,2}$')

    # Iterate through lines and extract numbers
    extracted_numbers = []
    for line in text.split('\n'):
        numbers = number_pattern.findall(line)
        extracted_numbers.extend(numbers)

    return extracted_numbers