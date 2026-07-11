import re 
from config.logging_config import get_logger

# Logging 
logger = get_logger(__name__)

def clean_resume_text(text):
    """
    Clean resume/JD text

    Args:
        text(str): Raw text to be cleaned.

    Returns:
        str: Cleaned text
    """

    logger.info("Cleaning resume text")
    
    try:
        ## lowercase 
        text = text.lower()
        #print('After lowercasing:', text)

        ## remove urls and domains
        text = re.sub(r'http\S+|www\S+|\S+\.(com|org|net|in)\S*', ' ', text)
        #print('After removing urls and domains:', text)

        ## remove emails
        text = re.sub(r'\S+@\S+', ' ', text)
        #print('After removing emails:', text)

        ## remove special chars
        text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
        #print('After removing special characters:', text)

        ## phone numbers
        text = re.sub(r'\+?\d[\d\s\-]{8,}\d', ' ', text)
        #print('After removing phone numbers:', text)

        ## remove extra spaces
        text = re.sub(r'\s+', ' ', text)
        #print('After removing extra spaces:', text)

        return text.strip()
    
    except Exception as e:
        logger.error("Error cleaning text: %s", e)
        raise

def count_words(text):
    """
    Count the number of words in the cleaned text.

    Args:
        text(str): Cleaned text.

    Returns:
        int: Number of words in the text.
    """

    return len(text.split())


from collections import Counter

def get_top_n_words(text, n=10):
    """
    Get the top n most common words in the cleaned text.

    Args:
        text(str): Cleaned text.
        n(int): Number of top words to return.

    Returns:
        list: List of top n most common words.
    """

    words = text.split()

    return Counter(words).most_common(n)