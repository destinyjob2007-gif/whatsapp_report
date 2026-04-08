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

# --- STYLING & TERMINAL INITIALIZATION ---
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
    
    print(f"{Fore.YELLOW}{Style.BRIGHT}[!] FIRST-TIME SETUP: GOOGLE SMTP AUTH{Style.RESET_ALL}")
    print(f"{Fore.WHITE}1. Go to: {Fore.CYAN}https://myaccount.google.com/security")
    print(f"{Fore.WHITE}2. Enable {Fore.GREEN}'2-Step Verification'{Fore.WHITE}.")
    print(f"{Fore.WHITE}3. Search for {Fore.GREEN}'App passwords'{Fore.WHITE} in the top search bar.")
    print(f"{Fore.WHITE}4. Create a name (e.g., 'ANON') and copy the {Fore.YELLOW}16-digit code{Fore.WHITE}.")
    print(f"{Fore.RED}NOTE: Use the 16-digit code, NOT your regular password.{Style.RESET_ALL}\n")
    
    email = input(f"{Fore.CYAN}Enter Gmail: {Fore.WHITE}")
    password = getpass.getpass(f"{Fore.CYAN}Enter App Password: {Fore.WHITE}")
    with open(CONFIG_FILE, "w") as f: f.write(f"{email}\n{password}")
    return email, password

def send_mail(user_email, user_pass, target, subject, body):
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
    print(f"{Fore.RED}Version: 2.9.0  {Fore.GREEN}Mode: Strike & Recovery Hybrid{Style.RESET_ALL}")
    print(f"{Fore.BLUE}[-] Input Buffer & UI Optimized {Style.RESET_ALL}\n")

# --- MAIN MISSION ENGINE ---
while True:
    show_banner()
    email, password = get_credentials()

    print(f"{Fore.WHITE}[01] BAN PROTOCOL (Heavy Strike)")
    print(f"[02] UNBAN PROTOCOL (High-Level Appeal)")
    print(f"[03] EXIT")
    
    main_choice = input(f"\n{Fore.YELLOW}Select Mode: {Fore.WHITE}")

    if main_choice == "01":
        num = input(f"\n{Fore.CYAN}[-] Target Number: {Fore.WHITE}")
        print(f"    [01] Mass Bot [02] Financial Fraud [03] Harassment [04] MALWARE")
        v_choice = input(f"    Choice: {Fore.WHITE}")
        
        scenarios = {
            "01": ("Permanent", "Automated API Abuse", "Target is utilizing sophisticated third-party automation tools and modified API clients to bypass platform-wide transmission limits. Technical logs confirm coordinated bulk spam distribution causing severe network degradation."),
            "02": ("Permanent", "Financial Fraud/Phishing", "CRITICAL: Account is impersonating official entities for large-scale credential harvesting. Immediate termination mandatory to prevent further financial theft and community risk."),
            "03": ("Permanent", "Severe Targeted Harassment", "Target is engaged in persistent, coordinated harassment and hate speech. Manual bypass of security blocks detected. Suspension required for platform safety."),
            "04": ("Immediate Permanent", "Critical Malware/RAT Distribution", "CRITICAL SECURITY BREACH: Account is distributing .APK payloads containing Remote Access Trojans. Immediate, non-negotiable permanent ban required for hardware protection.")
        }
        b_type, v_type, details = scenarios.get(v_choice, scenarios["01"])
        subject = f"ACTION REQUIRED: {b_type.upper()} BAN REQUEST [{num}]"
        body = f"--- OFFICIAL SECURITY ANALYSIS ---\nTARGET: {num}\nVIOLATION: {v_type}\n\nTECHNICAL EVIDENCE:\n{details}"
        
        if send_mail(email, password, num, subject, body):
            print(f"{Fore.GREEN}✅ Heavy Strike Deployed.{Style.RESET_ALL}")
        
    elif main_choice == "02":
        num = input(f"\n{Fore.CYAN}[-] Recovery Number: {Fore.WHITE}")
        print(f"    [01] Legal False Positive [02] Cyber-Victim [03] Business Impact")
        u_choice = input(f"    Choice: {Fore.WHITE}")
        
        if u_choice == "01":
            details = f"I am formally contesting the suspension of account {num}. Following a comprehensive device audit, it is clear this was a false-positive flag by an automated system. I request an immediate manual human review."
        elif u_choice == "02":
            details = f"URGENT SAFETY REPORT: I am a victim of a targeted cyber-attack. My account {num} was compromised by third-party malware. I have factory reset my hardware. Requesting restoration for security."
        else:
            details = f"Account {num} is a critical professional line. Suspension is causing measurable financial damage. Requesting expedited review by a senior supervisor to restore operational status."

        subject = f"URGENT APPEAL: Account Restoration Request - {num}"
        body = f"To the Support Team,\n\n{details}\n\nRespectfully."
        if send_mail(email, password, num, subject, body):
            print(f"{Fore.GREEN}✅ Recovery Request Deployed.{Style.RESET_ALL}")

    elif main_choice == "03":
        break

    # --- RE-ENGINEERED TIMER & INPUT HANDLER ---
    unlock_time = datetime.now() + timedelta(hours=12)
    print(f"\n{Fore.RED}[!] MONITORING ACTIVE. PRESS '0' AND ENTER TO RESET.{Style.RESET_ALL}")
    
    try:
        while datetime.now() < unlock_time:
            t_str = str(unlock_time - datetime.now()).split('.')[0]
            
            # Wipes the line before writing to ensure single-line UI
            sys.stdout.write(f"\r\033[K{Fore.YELLOW}[COUNTDOWN]: {t_str} {Fore.WHITE}| Type '0' to New Mission: ")
            sys.stdout.flush()
            
            # Robust input checking (1.0 second window)
            ready, _, _ = select.select([sys.stdin], [], [], 1.0)
            if ready:
                if sys.stdin.readline().strip() == "0":
                    print(f"\n{Fore.CYAN}[*] Resetting...{Style.RESET_ALL}")
                    break
    except KeyboardInterrupt:
        break
