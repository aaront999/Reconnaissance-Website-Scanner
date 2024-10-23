from tld import get_fld 
from urllib.parse import urlparse

# parses the url and checks if there was a scheme entered, otherwise throws an error
def get_domain_name(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        print("Invalid URL/Scheme Not Detected: Please enter full URL with 'HTTP://' or 'HTTPS://'")
    
    # gets the domain and suffix using the "get_fld" (get fully qualified domain) function
    domain_name = get_fld(url)
    return domain_name

# test cases
passed_url = "https://www.hackthissite.org"
print(f"Domain name: {get_domain_name(passed_url)}")

# failed_url = "www.hackthissite.org"
# print(f"Domain name: {get_domain_name(failed_url)}")