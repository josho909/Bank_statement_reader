def extract_dates_from_text(text):
    dates = []
    date_pattern = re.compile(r'^\d{2} \w{3}')
    
    for line in text.split('\n'):
        match = date_pattern.match(line)
        if match:
            dates.append(match.group())
            rollover = match.group()
        else: dates.append(rollover)

    return dates