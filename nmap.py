import os
from colorama import init, Fore, Style
import subprocess

def clear_screen():
    os.system('clear' if os.name == 't' else 'clear')

def install_nmap():
    print("Nmap is not found. Installing...")
    subprocess.run(["sudo", "apt", "update", "-y"])
    subprocess.run(["sudo", "apt", "install", "nmap", "-y"])

def check_nmap():
    try:
        subprocess.run(["nmap", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except FileNotFoundError:
        return False
    return True

def scan_host(host):
    print(f"Scanning host {host} for common ports...")
    subprocess.run(["nmap", "-F", "-T3", host])

def main():
    if not check_nmap():
        install_nmap()
    else:
        print("Nmap is already installed.")

    host = input("Enter the host to scan: ")
    scan_host(host)

if __name__ == "__main__":
    main()
