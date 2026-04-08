import smtplib
import requests
import time
import os
import getpass
import re
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
    email = input(f"{Fore.CYAN}Enter Gmail: {Fore.WHITE}")
    password = getpass.getpass(f"{Fore.CYAN}Enter App Password: {Fore.WHITE}")
    with open(CONFIG_FILE, "w") as f: f.write(f"{email}\n{password}")
    return email, password

def send_mail(user_email, user_pass, target, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = user_email
    msg['To'] = "support@whatsapp.com"
    msg.set_content(body)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(user_email, user_pass)
            smtp.send_message(msg)
        return True
    except: return False

def show_banner():
    os.system('clear')
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print(r" $$$$$$\  $$\   $$\  $$$$$$\  $$\   $$\ ")
    print(r"$$  __$$\ $$$\  $$ |$$  __$$\ $$ |  $$ |")
    print(r"$$ /  $$ |$$$$\ $$ |$$ /  $$ |$$ |  $$ |")
    print(r"$$$$$$$$ |$$ $$\$$ |$$ |  $$ |$$$$$$$$ |")
    print(r"$$  __$$ |$$ \$$$$ |$$ |  $$ |$$  __$$ |")
    print(r"$$ |  $$ |$$ |\$$$ |$$ |  $$ |$$ |  $$ |")
    print(r"$$ |  $$ |$$ | \$$ |\$$$$$$  |$$ |  $$ |")
    print(r"\__|  \__|\__|  \__| \______/ \__|  \__|")
    print(f"{Fore.RED}Version: 2.6.0  {Fore.GREEN}Mode: Single-Line Tactical UI{Style.RESET_ALL}")
    print(f"{Fore.BLUE}[-] Authority & Restoration Systems Online {Style.RESET_ALL}\n")

while True:
    show_banner()
    email, password = get_credentials()

    print(f"{Fore.WHITE}[01] BAN PROTOCOL (Heavy Strike)")
    print(f"[02] UNBAN PROTOCOL (High-Level Appeal)")
    print(f"[03] EXIT")
    
    main_choice = input(f"\n{Fore.YELLOW}Select Mode: {Fore.WHITE}")

    if main_choice == "01":
        num = input(f"\n{Fore.CYAN}[-] Target Number: {Fore.WHITE}")
        print(f"    [01] Mass Bot [02] Fraud [03] Harassment [04] MALWARE")
        v_choice = input(f"    Choice: {Fore.WHITE}")
        
        if v_choice == "01":
            v_type = "Automated Script Abuse"; details = "Target is utilizing sophisticated third-party automation tools and modified API clients to bypass platform-wide transmission limits. This activity is causing significant network degradation. Immediate permanent termination is required."
        elif v_choice == "02":
            v_type = "Organized Financial Fraud"; details = "CRITICAL: Account is impersonating official entities for large-scale credential harvesting and deploying malicious redirects to steal financial assets. Immediate permanent account termination is mandatory."
        elif v_choice == "03":
            v_type = "Severe Coordinated Harassment"; details = "Target is engaged in persistent, coordinated harassment and hate speech, utilizing unauthorized methods to bypass security block lists. Permanent suspension requested for user well-being."
        else:
            v_type = "Critical Malware Distribution"; details = "CRITICAL SECURITY BREACH: Account is distributing malicious .APK payloads (RATs/Spyware) designed to compromise device security and exfiltrate data. Immediate, non-negotiable permanent ban required."

        subject = f"ACTION REQUIRED: URGENT PERMANENT BAN REQUEST [{num}]"
        body = f"--- OFFICIAL SECURITY ANALYSIS ---\nTARGET: {num}\nVIOLATION: {v_type}\n\nTECHNICAL EVIDENCE:\n{details}"
        if send_mail(email, password, num, subject, body): print(f"{Fore.GREEN}✅ Heavy Strike Deployed.{Style.RESET_ALL}")
        
    elif main_choice == "02":
        num = input(f"\n{Fore.CYAN}[-] Recovery Number: {Fore.WHITE}")
        print(f"    [01] Legal False Positive [02] Cyber-Victim [03] Business Impact")
        u_choice = input(f"    Choice: {Fore.WHITE}")
        
        if u_choice == "01":
            details = f"I am formally contesting the suspension of account {num}. This was a clear false-positive flag by an automated system. I request an immediate manual human review and restoration."
        elif u_choice == "02":
            details = f"URGENT: I am a victim of a cyber-attack. My account {num} was compromised by third-party malware. I have secured my device and request restoration to prevent further identity misuse."
        else:
            details = f"Account {num} is a primary professional line. Its suspension is causing measurable financial damage. I request an expedited review to restore my professional standing."

        subject = f"URGENT APPEAL: Account Restoration Request - {num}"
        body = f"To the Support Team,\n\n{details}\n\nRespectfully."
        if send_mail(email, password, num, subject, body): print(f"{Fore.GREEN}✅ High-Level Recovery Request Deployed.{Style.RESET_ALL}")

    elif main_choice == "03": break

    # --- THE FIXED SINGLE-LINE TIMER ---
    unlock_time = datetime.now() + timedelta(hours=12)
    print(f"\n{Fore.RED}[!] PROTOCOL DEPLOYED. MONITORING...{Style.RESET_ALL}")
    
    while datetime.now() < unlock_time:
        t_str = str(unlock_time - datetime.now()).split('.')[0]
        
        # \033[K is the ANSI escape code to clear the rest of the line
        # This prevents the "ghosting" or duplication on mobile terminals
        sys.stdout.write(f"\r{Fore.YELLOW}[COUNTDOWN]: {t_str} {Fore.WHITE}| Type '0' to New Mission\033[K")
        sys.stdout.flush()
        
        r, _, _ = select.select([sys.stdin], [], [], 1)
        if r:
            if sys.stdin.readline().strip() == "0":
                print("\n" + Fore.CYAN + "[*] Mission Reset." + Style.RESET_ALL)
                break
