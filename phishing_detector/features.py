import re
import socket
from urllib.parse import urlparse
from datetime import datetime

import tldextract
import whois


def has_ip_address(url: str) -> bool:
    """
    To Check if the domain in the URL is an IP address.
    Phishing URLs sometimes use raw IPs to avoid detection.
    """
    try:
        return bool(re.match(r'https?://(\d{1,3}\.){3}\d{1,3}', url))
    except:
        return False


def count_digits(url: str) -> int:
    """It will Count how many digits are in the entire URL."""
    return sum(char.isdigit() for char in url)


def count_special_characters(url: str) -> int:
    """
    It can Count special characters in the URL.
   Even Phishing URLs often contain special characters to obfuscate or trick users.
    """
    return len(re.findall(r'[^\w]', url))  # Not a-z, A-Z, 0-9, or underscore


def get_domain_age(domain: str) -> int:
    """
    Return the age of the domain in days.
    Phishing domains are often newly registered.
    Returns -1 if domain age cannot be determined.
    """
    try:
        whois_data = whois.whois(domain)
        creation_date = whois_data.creation_date

        # Sometimes returned as a list
        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if not creation_date:
            return -1

        age_in_days = (datetime.now() - creation_date).days
        return age_in_days
    except:
        return -1  # WHOIS lookup failed


def extract_features(url: str) -> list:
    """
    Extracts advanced features from a URL for use in phishing detection models.
    Returns a list of numeric features.
    """

    parsed_url = urlparse(url)
    extracted = tldextract.extract(url)

    # Full domain (e.g., "google.com")
    domain = f"{extracted.domain}.{extracted.suffix}" if extracted.suffix else parsed_url.netloc

    # Common phishing-related keywords
    suspicious_keywords = ['login', 'secure', 'account', 'update', 'banking']

    # Feature vector - using the 6 most important features for phishing detection
    features = [
        len(url),  # 0: Total length of the URL
        url.count('.'),  # 1: Number of dots in the URL
        int('@' in url),  # 2: '@' symbol present
        int(has_ip_address(url)),  # 3: Uses IP address instead of domain
        int(any(keyword in url.lower() for keyword in suspicious_keywords)),  # 4: Suspicious keywords present
        count_special_characters(url),  # 5: Count of special characters
    ]

    return features
