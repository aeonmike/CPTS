import os
from colorama import init, Fore, Style
import subprocess

def clear_screen():
    os.system('clear' if os.name == 't' else 'clear')

def windows_attack():
    print_banner()
    clear_screen()
    subprocess.run(["python3", "windows.py"])


def windows_attack():
    print_banner()
    clear_screen()
    subprocess.run(["python3", "linux.py"])


def web_app_attack():
    print("Performing Web App attack...")
    # Add your Web App attack code here

def main_menu():
    while True:
        clear_screen()
        print("Main Menu:")
        print("1. Windows Attack")
        print("2. Linux Attack")
        print("3. Web App Attack")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            windows_attack()
            input("Press Enter to continue.")
        elif choice == "2":
            linux_attack()
            input("Press Enter to continue.")
        elif choice == "3":
            web_app_attack()
            input("Press Enter to continue.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            input("Invalid option. Press Enter to continue.")

if __name__ == "__main__":
    main_menu()
