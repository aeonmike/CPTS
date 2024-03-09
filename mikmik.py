
def print_banner():
    init(autoreset=True)
    banner = """

░▒▓██████████████▓▒░  ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓███████▓▒░  ░▒▓██████▓▒░   
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░ 
                                                            
Security Framework V.1                                                            
Author --- Mike Cabalin
    """
    print(Fore.GREEN + banner)


import os
from colorama import init, Fore, Style
import subprocess

def clear_screen():
    os.system('clear' if os.name == 't' else 'clear')

def scan():
    clear_screen()
    print_banner()
    subprocess.run(["python3", "scan.py"])

def attack():
    clear_screen()
    print_banner()
    subprocess.run(["python3", "attack.py"])

def main():
    while True:
        clear_screen()
        print_banner()
        # Display menu options
        print("Menu:")
        print("1. Scan")
        print("2. Attack")
        print("3. Exit")

        # Ask for user input
        choice = input("Choose an option: ")

        # Process user choice
        if choice == "1":
            scan()
        elif choice == "2":
            attack()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()

