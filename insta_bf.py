import os
import sys
import time
import random
import webbrowser
from colorama import Fore, init
from pyfiglet import Figlet

init(autoreset=True)  # Colorama init

def check_subscription():
    subscribed = False
    print(Fore.YELLOW + "\n[!] Pehle mere YouTube channel ko subscribe karo!")
    print(Fore.CYAN + "[+] Channel: https://www.youtube.com/@Tayyabexploits\n")
    
    while True:
        ans = input(Fore.GREEN + "[?] Kya aap ne subscribe kar liya? (haan/na): ").lower()
        if ans == "haan":
            print(Fore.GREEN + "\n[✓] Shukriya! Tool use karne ke liye taiyar hai!\n")
            time.sleep(2)
            return True
        else:
            print(Fore.RED + "\n[✗] Tool tab tak kaam nahi karega jab tak subscribe nahi karoge!\n")

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    custom_fig = Figlet(font='slant')
    print(Fore.MAGENTA + custom_fig.renderText('INSTA  BF'))

def bruteforce_attack():
    username = input(Fore.CYAN + "\n[?] Instagram username enter karo: ")
    print(Fore.YELLOW + f"\n[!] {username} par brute force shuru...")
    
    # Fake loading simulation
    for _ in range(3):
        print(Fore.YELLOW + "[+] Generating 12-digit passwords...")
        time.sleep(1)
    
    # Generate random password
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    print(Fore.RED + f"\n[!] Password cracked nahi hua! Yeh try karo: {password} (Fake Demo)")

def whatsapp_option():
    print(Fore.GREEN + "\n[+] WhatsApp channel mein redirect ho raha hai...")
    webbrowser.open("https://whatsapp.com/channel/0029VanMDac05MUliOn3T52n")

def main_menu():
    while True:
        show_banner()
        print(Fore.CYAN + """
1. Bruteforce Start 
2. WhatsApp Channel Join Karein
3. OUR website 
4. Exit Tool
        """)
        
        choice = input(Fore.YELLOW + "\n[?] Apna option chuniye (1-4): ")
        
        if choice == "1":
            bruteforce_attack()
        elif choice == "2":
            whatsapp_option()
        elif choice == "3":
            print(Fore.MAGENTA + "\n[+] Coming Soon... Stay Tuned!")
        elif choice == "4":
            print(Fore.RED + "\n[!] Tool se bahar ja rahe hain...")
            sys.exit()
        else:
            print(Fore.RED + "\n[!] Galat option! Phir se try karein.")
        
        input("\n[Press Enter to continue...]")

if __name__ == "__main__":
    if check_subscription():
        main_menu()