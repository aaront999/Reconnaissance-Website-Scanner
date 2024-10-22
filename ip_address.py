import socket

def get_ip_address(url):
    # removes "http://" and "https://" from the url and splits the domain and paths by "/"
    # and only uses index 0 (the domain)  
    hostname = url.replace("http://", "").replace("https://", "").split("/")[0]

    # tries to get the ip address of the domain, if it can't resolve, throws an error
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return {"Invalid URL or unable to resolve DNS."}

url = "https://www.hackthissite.org/"
print(f"IP Address of {url} is: {get_ip_address(url)}")
        