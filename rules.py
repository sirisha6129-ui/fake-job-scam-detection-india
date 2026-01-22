# rules.py
from text_clean import clean_text  # no folder, just import

def is_scam(text):
    text = clean_text(text)
    scam_keywords = ["fake", "scam", "offer", "urgent"]
    for word in scam_keywords:
        if word in text:
            return True
    return False