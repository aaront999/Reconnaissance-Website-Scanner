import os
import whois

def get_whois(url):
    whois_results = whois.whois(url)
    return str(whois_results)

# test cases
test_url = "hackthissite.org"
print(get_whois(test_url))