from urllib.parse import urlparse
import re


TRUSTED_DOMAINS = [
    "sbi.co.in",
    "google.com",
    "microsoft.com",
    "paypal.com",
    "amazon.in",
    "amazon.com",
    "icicibank.com",
    "hdfcbank.com",
    "axisbank.com"
]


def extract_urls(text):

    pattern = r"https?://[^\s]+"

    return re.findall(pattern, text)


def analyze_url(url):

    domain = urlparse(url).netloc.lower()

    warnings = []

    if any(domain.endswith(d) for d in TRUSTED_DOMAINS):

        return {
            "url": url,
            "domain": domain,
            "safe": True,
            "warnings": []
        }

    if "-" in domain:
        warnings.append("Hyphen found in domain")

    if domain.endswith(".xyz"):
        warnings.append("Uses uncommon .xyz domain")

    if len(domain.split(".")) > 3:
        warnings.append("Too many subdomains")

    if "secure" in domain:
        warnings.append("Uses security-related keyword to appear legitimate")

    return {
        "url": url,
        "domain": domain,
        "safe": False,
        "warnings": warnings
    }