import re

def is_valid_url(url):
    """
    Check if the passed parameter is a valid URL.

    Args:
    - url (str): The URL to check.

    Returns:
    - bool: True if the URL is valid, False otherwise.
    """
    url_pattern = re.compile(r"^https?://(?:www\.)?\w+\.\w{2,3}$")
    if url_pattern.match(url):
        return True
    else:
        return False

url = "http://www.midtermmateolariosexample.com"
print(is_valid_url(url))  # Output: True

url = "invalid-url"
print(is_valid_url(url))  # Output: False
