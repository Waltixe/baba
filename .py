import os
import platform
import socket
import whois
import urllib
import subprocess
import psutil
from termcolor import colored

# Gets system info
def get_system_info():
    system_info = "System: {0}\nOS: {1}\nKernel Version: {2}\nCPU: {3}\nRAM: {4}\nDisk Space: {5}".format(
        platform.system(),
        platform.release(),
        platform.version(),
        platform.processor(),
        psutil.virtual_memory().percent,
        psutil.disk_usage('/').percent
    )
    return system_info

# Gets current ip address
def get_current_ip():
    try:
        current_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        return current_ip
    except Exception as e:
        return str(e)

# Gets DNS information
def get_dns_info():
    try:
        dns_info = str(socket.gethostbyname(socket.gethostname()))
        return dns_info
    except Exception as e:
        return str(e)

# Gets domain registration info
def get_domain_info(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return str(e)

# Gets geolocation information
def get_geolocation_info(ip_address):
    try:
        response = urllib.request.urlopen('http://ip-api.com/json/{}'.format(ip_address))
        data = response.read()
        encoding = response.info().get_content_charset('utf-8')
        geolocation_info = json.loads(data.decode(encoding))
        return geolocation_info
    except Exception as e:
        return str(e)

# Gets system process info
def get_process_info():
    try:
        process_info = str(psutil.process_iter(['pid', 'name', 'username']))
        return process_info
    except Exception as e:
        return str(e)

# Gets network connection info
def get_network_info():
    try:
        network_info = str(psutil.net_connections())
        return network_info
    except Exception as e:
        return str(e)

# Gets running services info
def get_service_info():
    try:
        service_info = str(subprocess.check_output(['systemctl', 'list-units', '--type=service']))
        return service_info
    except Exception as e:
        return str(e)

def main():
    osint_results = []
    system_info = get_system_info()
    osint_results.append(colored("System Information:", 'yellow'))
    osint_results.append(system_info)

    current_ip = get_current_ip()
    osint_results.append(colored("\nCurrent IP Address:", 'yellow'))
    osint_results.append(current_ip)

    dns_info = get_dns_info()
    osint_results.append(colored("\nDNS Information:", 'yellow'))
    osint_results.append(dns_info)

    domain = input(colored("\nEnter a domain to get registration info:", 'green'))
    domain_info = get_domain_info(domain)
    osint_results.append(colored("\nDomain Registration Information:", 'yellow'))
    osint_results.append(domain_info)

    ip_address = input(colored("\nEnter an IP address to get geolocation info:", 'green'))
    geolocation_info = get_geolocation_info(ip_address)
    osint_results.append(colored("\nGeolocation Information:", 'yellow'))
    osint_results.append(geolocation_info)

    osint_results.append(colored("\nProcess Information:", 'yellow'))
    osint_results.append(get_process_info())

    osint_results.append(colored("\nNetwork Connection Information:
