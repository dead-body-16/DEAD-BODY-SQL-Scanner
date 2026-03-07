import requests, sys, webbrowser, os, time

# Colors
G, R, W, B, Y, C = '\033[92m', '\033[91m', '\033[0m', '\033[94m', '\033[93m', '\033[36m'
BOLD = '\033[1m'

def banner():
    os.system('clear')
    print(f"""
{B}{BOLD}=================================================
       SUBDOMAIN RECON - PRO EDITION
           Created by: NZ NISHAN
================================================={W}""")

def setup_github():
    print(f"\n{Y}[*] Configuring git repository...{W}")
    time.sleep(2)
    os.system('git init')
    with open('README.md', 'w') as f: f.write("# Subdomain-Recon-Pro\n\nCreated by: NZ NISHAN")
    print(f"{G}[+] Git initialized successfully!{W}")
    input("\nPress Enter to return...")

def get_subdomains(domain):
    print(f"\n{Y}[*] Initiating deep scan for: {domain}{W}")
    time.sleep(2)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(f"https://crt.sh/?q={domain}&output=json", headers=headers, timeout=20)
        subdomains = sorted(list(set(entry['common_name'] for entry in response.json())))
        print(f"\n{G}[+] Found {len(subdomains)} results.{W}")
        for sub in subdomains: print(f"{G}[!] {W}{sub}")
    except Exception as e: print(f"{R}[!] Error: {e}{W}")

def main():
    while True:
        banner()
        print(f"{G}1. Scan Subdomains")
        print(f"2. Follow boycott_nishan (Instagram)")
        print(f"3. Auto-Setup Github Repo")
        print(f"4. Exit{W}")
        
        choice = input(f"\n{Y}Select an option [1-4]: {W}")
        if choice == '1':
            target = input(f"{Y}[?] Enter domain: {W}")
            get_subdomains(target)
            input(f"\n{B}Press Enter to return...{W}")
        elif choice == '2':
            webbrowser.open('https://www.instagram.com/boycott_nishan/')
        elif choice == '3':
            setup_github()
        elif choice == '4':
            sys.exit()
        else:
            print(f"{R}Invalid choice!{W}")

if __name__ == "__main__":
    main()
