import requests
import os
import time
import sys

# Colors
G = '\033[1;32m'
R = '\033[1;31m'
B = '\033[1;34m'
Y = '\033[1;33m'
W = '\033[0m'
BOLD = '\033[1m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def type_effect(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def loading():
    clear()
    print(f"{R}[!] INITIALIZING DEAD BODY SYSTEM...{W}")
    # Simple loading animation
    for i in range(5):
        time.sleep(0.5)
        sys.stdout.write(".")
        sys.stdout.flush()
    print(f"\n{G}[+] SYSTEM READY!{W}\n")
    time.sleep(1)

def show_banner(title):
    clear()
    print(f"{R}{BOLD}")
    print("  ██████╗ ███████╗ █████╗ ██████╗     ██████╗  ██████╗ ██████╗ ██╗   ██╗")
    print("  ██╔══██╗██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝")
    print("  ██║  ██║█████╗  ███████║██║  ██║    ██████╔╝██║   ██║██║  ██║ ╚████╔╝ ")
    print("  ██║  ██║██╔══╝  ██╔══██║██║  ██║    ██╔══██╗██║   ██║██║  ██║  ╚██╔╝  ")
    print("  ██████╔╝███████╗██║  ██║██████╔╝    ██████╔╝╚██████╔╝██████╔╝   ██║   ")
    print("  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝     ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝   ")
    print(f"{G}{'='*67}")
    print(f"  MODE: {title}")
    print(f"{G}{'='*67}{W}\n")

def run_scanner():
    show_banner("SQL VULNERABILITY SCANNER")
    target = input(f"{Y}[?] ENTER TARGET URL: {W}")
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    payloads = ["'", '"', "';--", "UNION SELECT 1,2,3--"]
    
    print(f"{B}[*] SCANNING STARTED...{W}")
    
    found = False
    for p in payloads:
        print(f"{Y}[>] Testing: {p}{W}")
        try:
            res = requests.get(target + p, headers=headers, timeout=5)
            if any(err in res.text.lower() for err in ["sql syntax", "mysql", "postgresql"]):
                print(f"{G}[!!!] VULNERABILITY FOUND WITH PAYLOAD: {p}{W}")
                found = True
                break
        except: continue
        
    if not found:
        print(f"{R}[-] TARGET SECURE.{W}")
    
    input(f"\n{B}Press [ENTER] to return...{W}")

def main():
    loading()
    while True:
        show_banner("MAIN TERMINAL")
        print(f"  [01] START SCAN\n  [02] ABOUT\n  [03] EXIT")
        choice = input(f"\n{Y}DEAD-BODY@TERMINAL:~# {W}")
        if choice == '1': run_scanner()
        elif choice == '2':
            print("  DEVELOPED BY: NZ NISHAN")
            input("\nPress [ENTER]...")
        elif choice == '3': sys.exit()

if __name__ == "__main__":
    main()
