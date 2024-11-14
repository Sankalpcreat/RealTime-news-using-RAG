# utils/token_manager.py
import tiktoken

MAX_TOKENS = 2048  # Adjust based on your model's token limits
encoding = tiktoken.get_encoding("gpt-3.5-turbo")  # Replace with the model name you're using

def truncate_text(text):
    tokens = encoding.encode(text)
    if len(tokens) > MAX_TOKENS:
        return encoding.decode(tokens[:MAX_TOKENS])
    return text
