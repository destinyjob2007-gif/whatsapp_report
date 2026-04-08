import smtplib
import time
import os
import getpass
import sys
import select
from email.message import EmailMessage
from datetime import datetime, timedelta

# --- STYLING ---
try:
    from colorama import init, Fore, Style
    init() 
except ImportError:
    class Fore: RED = GREEN = YELLOW = BLUE = CYAN = WHITE = RESET = ''
    class Style: BRIGHT = RESET_ALL = ''

CONFIG_FILE = ".env"

def get_credentials():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            lines = f.readlines()
            if len(lines) >= 2: return lines[0].strip(), lines[1].strip()
    print(f"{Fore.YELLOW}[!] Setup Required. Use a 16-digit Google App Password.{Style.RESET_ALL}")
    email = input(f"{Fore.CYAN}Enter Gmail: {Fore.WHITE}")
    password = getpass.getpass(f"{Fore.CYAN}Enter App Password: {Fore.WHITE}")
    with open(CONFIG_FILE, "w") as f: f.write(f"{email}\n{password}")
    return email, password

def send_mail(user_email, user_pass, target_num, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = user_email
    msg['To'] = "support@support.whatsapp.com"
    msg.set_content(body)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(user_email, user_pass)
            smtp.send_message(msg)
        return True
    except: return False

def handle_automation(body):
    """Displays report for manual copy and triggers browser in background."""
    print(f"\n{Fore.YELLOW}--- COPY THE TEXT BELOW ---{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{body}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}--- END OF REPORT ---{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}[*] Opening Browser... Copy the text above now!{Style.RESET_ALL}")
    
    url = "https://www.whatsapp.com/contact/noclient/"
    # Background launch to prevent Termux hanging
    os.system(f'nohup termux-open-url {url} > /dev/null 2>&1 &')
    
    # 5-second window to copy before the countdown starts
    time.sleep(5)

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print(r" $$$$$$\  $$\   $$\  $$$$$$\  $$\   $$\ ")
    print(r"$$  __$$\ $$$\  $$ |$$  __$$\ $$ |  $$ |")
    print(r"$$ /  $$ |$$$$\ $$ |$$ /  $$ |$$ |  $$ |")
    print(r"$$$$$$$$ |$$ $$\$$ |$$ |  $$ |$$$$$$$$ |")
    print(r"$$  __$$ |$$ \$$$$ |$$ |  $$ |$$  __$$ |")
    print(r"$$ |  $$ |$$ |\$$$ |$$ |  $$ |$$ |  $$ |")
    print(r"$$ |  $$ |$$ | \$$ |\$$$$$$  |$$ |  $$ |")
    print(r"\__|  \__|\__|  \__| \______/ \__|  \__|")
    print(f"{Fore.RED}Version: 3.1.7  {Fore.GREEN}Mode: 6H Tactical Strike{Style.RESET_ALL}")
    print(f"{Fore.BLUE}[-] Zero-Tolerance Protocols Active {Style.RESET_ALL}\n")

while True:
    show_banner()
    email, password = get_credentials()

    print(f"{Fore.WHITE}[01] BAN PROTOCOL")
    print(f"[02] UNBAN PROTOCOL")
    print(f"[03] EXIT")
    
    main_choice = input(f"\n{Fore.YELLOW}Select Mode: {Fore.WHITE}")

    if main_choice == "01":
        num = input(f"\n{Fore.CYAN}[-] Target Number: {Fore.WHITE}")
        print(f"    [01] Spam [02] Fraud [03] Sexual [04] MALWARE")
        v_choice = input(f"    Choice: {Fore.WHITE}")
        
        v_map = {
            "01": "Coordinated Bulk Spam",
            "02": "Financial Fraud & Phishing",
            "03": "Unsolicited Sexual Content",
            "04": "Malware & RAT Distribution"
        }
        violation = v_map.get(v_choice, "Terms of Service Violation")

        subject = f"CRITICAL: Cybercrime Complaint - [{num}]"
        
        full_body = f"""To the WhatsApp Trust and Safety Team,

This is a formal cybercrime report regarding account {num}. 

INCIDENT SUMMARY:
The account is engaging in criminal activity categorized as {violation}. 

TECHNICAL EVIDENCE:
The account utilizes social engineering and malicious URLs to steal credentials and distribute unauthorized RAT software.

REQUEST:
Immediate manual investigation and permanent account termination.

Sincerely,
Digital Safety Enforcement Liaison"""

        if send_mail(email, password, num, subject, full_body):
            print(f"{Fore.GREEN}✅ Email Sent.{Style.RESET_ALL}")
        
        handle_automation(full_body)
        
    elif main_choice == "02":
        num = input(f"\n{Fore.CYAN}[-] Recovery Number: {Fore.WHITE}")
        subject = f"APPEAL: Account Review Request - {num}"
        body = f"To WhatsApp Support, I request a manual review of account {num}. Flagged in error."
        if send_mail(email, password, num, subject, body):
            print(f"{Fore.GREEN}✅ Appeal Sent.{Style.RESET_ALL}")
        handle_automation(body)

    elif main_choice == "03": break

    # --- 6-HOUR MONITORING PROTOCOL ---
    unlock_time = datetime.now() + timedelta(hours=6)
    print(f"\n{Fore.RED}[!] MONITORING ACTIVE. PRESS '0' TO RESET.{Style.RESET_ALL}")
    try:
        while datetime.now() < unlock_time:
            t_str = str(unlock_time - datetime.now()).split('.')[0]
            sys.stdout.write(f"\r\033[K{Fore.YELLOW}[WAITING]: {t_str} {Fore.WHITE}| COMMAND: ")
            sys.stdout.flush()
            ready, _, _ = select.select([sys.stdin], [], [], 1.0)
            if ready:
                if sys.stdin.readline().strip() == "0": break
    except KeyboardInterrupt: break
