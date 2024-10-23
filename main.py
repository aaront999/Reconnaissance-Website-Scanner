from general import *
from domain_name import *
from ip_address import *
from nmap_scan import *
from whois_lookup import *

ROOT_DIR = 'Targets'
create_dir(ROOT_DIR)

def scan_data(name, full_url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(url)
    nmap_results = get_nmap_scan('-F', ip_address)
    whois_results = get_whois(domain_name)
    scan_results(name, full_url, domain_name, ip_address, nmap_results, whois_results)

def scan_results(name, full_url, domain_name, ip_address, nmap_results, whois_results):
    scanned_dir = ROOT_DIR + "/" + name
    create_dir(scanned_dir)
    write_file(scanned_dir + '/full_url.txt', full_url)
    write_file(scanned_dir + '/domain_name.txt', domain_name)
    write_file(scanned_dir + '/ip_address.txt', ip_address)
    write_file(scanned_dir + '/nmap_results.txt', nmap_results)
    write_file(scanned_dir + '/whois_results.txt', whois_results)

     
scan_data('hackthissite', 'https://www.hackthissite.org')