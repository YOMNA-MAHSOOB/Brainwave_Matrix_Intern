import re 
import difflib
from urllib.parse import urlparse 

'''
Common signs of phishing links:
1-Contains IP address
2-Misspelled domains like "faceb00k" instead of "facebook"
3-Too long / confusing
4-Suspicious characters [@, %, =, & in the middle of the link]
5-No HTTPS : [ http:// instead of https:// ]
'''

# 1
def contains_IP(url):
    pattern= r"(https?:\/\/)?\d{1,3}(\.\d{1,3}){3}"
    return re.search(pattern,url) is not None
# 2
def Misspelled_domains(url):
    # e.g
    trusted_domains = ["google.com", "facebook.com", "microsoft.com", "amazon.com", "youtube.com"]
    domain= urlparse(url).netloc.lower()
    domain = domain.replace("www.", "")
    matches=difflib.get_close_matches(domain, trusted_domains,n=1, cutoff=0.8)
    return len(matches)> 0 and domain not in trusted_domains
# 3
def long_url(url):
    return len(url)>100

# 4
def contains_Suspicious_characters(url):
    return any(char in url for char in ['@', '%', '=', '&'])
# 5
def has_https(url):
    return url.startswith("https://")


