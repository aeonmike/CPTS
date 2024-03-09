import os
from colorama import init, Fore, Style
import subprocess

def clear_screen():
    os.system('clear' if os.name == 't' else 'clear')

def nmap():
    print_banner()
    clear_screen()
    subprocess.run(["python3", "nmap.py"])


def scan():
    while True:
        # Display menu options
        print("Scan Menu:")
        print("1. nmap")
        print("2. nikto")
        print("3. wapiti")
        print("4. sqlmap")
        print("5. skipfish")
        print("6. Exit")

        # Ask for user input
        choice = input("Choose a scanning tool (1-6): ")

        # Process user choice
        if choice == "1":
            os.system("python3 nmap.py")  # Execute nmap
        elif choice == "2":
            os.system("nikto")  # Execute nikto
        elif choice == "3":
            os.system("mapiti")  # Execute mapiti
        elif choice == "4":
            os.system("sqlmap")  # Execute sqlmap
        elif choice == "5":
            os.system("skipfish")  # Execute skipfish
        elif choice == "6":
            print("Exiting scan menu...")
            break
        else:
            print("Invalid option. Please choose again.")

# Test the scan function
scan()
