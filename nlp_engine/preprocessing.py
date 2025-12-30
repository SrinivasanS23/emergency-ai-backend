import re

def clean_text(text: str) -> str:
    """
    Cleans input text for NLP processing.
    - Lowercases text
    - Removes URLs
    - Removes special characters and numbers
    - Removes extra whitespace
    """

    if not isinstance(text, str):
        return ""

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove numbers and special characters
    text = re.sub(r"[^a-z\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text
