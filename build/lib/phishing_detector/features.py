from urllib.parse import urlparse
import tldextract

def extract_features(url: str) -> list:
    """Extract simple features from the URL for ML model."""
    parsed = urlparse(url)
    ext = tldextract.extract(url)
    
    features = [
        len(url),  # Length of the URL
        url.count('.'),  # Number of dots in the URL    
        int('@' in url),  # Presence of '@' symbol and use of it
        int(parsed.scheme == 'https'),  # Is HTTPS used or not
        len(parsed.netloc),  # Length of the domain
        len(ext.subdomain),  # Length of subdomain
    ]
    return features