import re

def extract_dates_from_text(text):
    # Define date pattern to be extracted
    dates = []
    date_pattern = re.compile(r'^\d{2} \w{3}')
    
    # Iterate through lines and extract the date pattern
    for line in text.split('\n'):
        match = date_pattern.match(line)
        if match:
            dates.append(match.group())
            rollover = match.group()
        else: dates.append(rollover)

    return dates