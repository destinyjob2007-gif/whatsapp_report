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
    """Handles secure credential retrieval with a built-in help guide."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            lines = f.readlines()
            if len(lines) >= 2:
                return lines[0].strip(), lines[1].strip()
    
    # --- BUILT-IN USER GUIDE FOR FIRST-TIME USERS ---
    print(f"{Fore.YELLOW}{Style.BRIGHT}[!] FIRST-TIME SETUP: GOOGLE SMTP AUTH{Style.RESET_ALL}")
    print(f"{Fore.WHITE}1. Go to: {Fore.CYAN}https://myaccount.google.com/security")
    print(f"{Fore.WHITE}2. Enable {Fore.GREEN}'2-Step Verification'{Fore.WHITE}.")
    print(f"{Fore.WHITE}3. Search for {Fore.GREEN}'App passwords'{Fore.WHITE} in the top search bar.")
    print(f"{Fore.WHITE}4. Create a name (e.g., 'ANON') and copy the {Fore.YELLOW}16-digit code{Fore.WHITE}.")
    print(f"{Fore.RED}NOTE: Do NOT use your regular Gmail password. It will not work.{Style.RESET_ALL}\n")
    
    email = input(f"{Fore.CYAN}Enter Gmail Address: {Fore.WHITE}")
    # Using getpass hides the password as the user types it for security
    password = getpass.getpass(f"{Fore.CYAN}Enter 16-Digit App Password: {Fore.WHITE}")
    
    with open(CONFIG_FILE, "w") as f:
        f.write(f"{email}\n{password}")
    return email, password

def send_mail(user_email, user_pass, target, subject, body):
    """Core SMTP Engine for sending the tactical reports."""
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
    except Exception as e:
        print(f"\n{Fore.RED}[X] SMTP Error: {e}{Style.RESET_ALL}")
        return False

def show_banner():
    """Tactical ASCII Banner."""
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
    print(f"{Fore.RED}Version: 2.7.0  {Fore.GREEN}Mode: Strike & Recovery Hybrid{Style.RESET_ALL}")
    print(f"{Fore.BLUE}[-] Authority & Restoration Protocols Active {Style.RESET_ALL}\n")

# --- MAIN MISSION LOOP ---
while True:
    show_banner()
    email, password = get_credentials()

    print(f"{Fore.WHITE}[01] BAN PROTOCOL (Heavy Strike)")
    print(f"[02] UNBAN PROTOCOL (High-Level Appeal)")
    print(f"[03] EXIT")
    
    main_choice = input(f"\n{Fore.YELLOW}Select Mode: {Fore.WHITE}")

    if main_choice == "01":
        num = input(f"\n{Fore.CYAN}[-] Target Number (with Country Code): {Fore.WHITE}")
        print(f"    [01] Mass Bot/Spam [02] Financial Fraud [03] Coordinated Harassment [04] MALWARE")
        v_choice = input(f"    Choice: {Fore.WHITE}")
        
        # --- LONG-FORM TECHNICAL EVIDENCE LOGS ---
        if v_choice == "01":
            v_type = "Automated Script Abuse"; details = "Target is utilizing sophisticated third-party automation tools and modified API clients to bypass platform-wide transmission limits. This activity is causing significant network degradation and community-wide disruption. Captured traffic logs indicate a coordinated effort to facilitate bulk spam distribution. Immediate permanent termination is required."
        elif v_choice == "02":
            v_type = "Organized Financial Fraud"; details = "CRITICAL: Account is impersonating official banking entities for large-scale credential harvesting and deploying malicious redirects to steal financial assets. This organized fraudulent campaign poses an imminent safety risk. Immediate permanent account termination is mandatory."
        elif v_choice == "03":
            v_type = "Severe Coordinated Harassment"; details = "Target is engaged in persistent, coordinated harassment and hate speech, utilizing unauthorized methods to bypass security block lists. This behavior violates safety guidelines regarding user well-being. Permanent suspension requested."
        else:
            v_type = "Critical Malware Distribution"; details = "CRITICAL SECURITY BREACH: Account is distributing malicious .APK payloads containing Remote Access Trojans (RATs) designed to compromise mobile device security and exfiltrate private user data. This is a severe criminal security risk. Immediate, non-negotiable permanent ban required."

        subject = f"ACTION REQUIRED: URGENT PERMANENT BAN REQUEST [{num}]"
        body = f"--- OFFICIAL SECURITY ANALYSIS ---\nTARGET: {num}\nVIOLATION: {v_type}\n\nTECHNICAL EVIDENCE:\n{details}\n\nCONCLUSION:\nA manual override and permanent ban are necessary to ensure the safety of the network."
        
        if send_mail(email, password, num, subject, body):
            print(f"{Fore.GREEN}✅ Heavy Strike Deployed.{Style.RESET_ALL}")
        
    elif main_choice == "02":
        num = input(f"\n{Fore.CYAN}[-] Recovery Number (with Country Code): {Fore.WHITE}")
        print(f"    [01] Legal False Positive [02] Cyber-Victim [03] Business Impact")
        u_choice = input(f"    Choice: {Fore.WHITE}")
        
        # --- PERSUASIVE LONG-FORM APPEALS ---
        if u_choice == "01":
            details = f"I am formally contesting the suspension of account {num}. Following an audit, it is clear this was a false-positive flag by an automated system. I have strictly adhered to all Terms of Service. I request an immediate manual human review and restoration of my digital identity."
        elif u_choice == "02":
            details = f"URGENT: I am a victim of a targeted cyber-attack. My account {num} was compromised by third-party malware which used my device without consent. I have since factory reset my hardware. I request restoration so I can secure my account properly."
        else:
            details = f"Account {num} is a critical professional communication line. Its current suspension is causing measurable financial damage and severe business interruption. I request an expedited review by a senior supervisor to restore service access."

        subject = f"URGENT APPEAL: Account Restoration Request - {num}"
        body = f"To the Support & Safety Department,\n\n{details}\n\nRespectfully."
        
        if send_mail(email, password, num, subject, body):
            print(f"{Fore.GREEN}✅ High-Level Recovery Request Deployed.{Style.RESET_ALL}")

    elif main_choice == "03":
        print(f"{Fore.BLUE}[-] Protocol Terminated.{Style.RESET_ALL}")
        break

    # --- THE FIXED SINGLE-LINE TICKING TIMER ---
    unlock_time = datetime.now() + timedelta(hours=12)
    print(f"\n{Fore.RED}[!] PROTOCOL QUEUED. MONITORING ACTIVE...{Style.RESET_ALL}")
    
    while datetime.now() < unlock_time:
        t_str = str(unlock_time - datetime.now()).split('.')[0]
        # \033[K clears the line to prevent duplication ghosting
        sys.stdout.write(f"\r{Fore.YELLOW}[COUNTDOWN]: {t_str} {Fore.WHITE}| Type '0' to New Mission\033[K")
        sys.stdout.flush()
        
        r, _, _ = select.select([sys.stdin], [], [], 1)
        if r:
            if sys.stdin.readline().strip() == "0":
                print(f"\n{Fore.CYAN}[*] Mission Resetting...{Style.RESET_ALL}")
                break
