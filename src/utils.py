import re

def sanitize_input(text):
    
    sanitized_text = re.sub(r'[^\w\s\-]', '', text)
    return sanitized_text.strip()
