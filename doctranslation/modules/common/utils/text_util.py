from langdetect import detect

def detect_language(text):
    """
    Detects the language of the input text.
    
    Parameters:
        text (str): The input text.
        
    Returns:
        str: The detected language code (e.g., 'en' for English).
    """
    return detect(text)
