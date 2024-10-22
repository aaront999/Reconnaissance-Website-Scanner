from tld import get_tld

# gets the domain and suffix using the "get_tld" function
def get_domain_name(url):
    domain_name = get_tld(url, as_object=True)
    return f"{domain_name.domain}.{domain_name.suffix}"

# test cases
url = "https://www.hackthissite.org/"
print(f"Domain name: {get_domain_name(url)}")