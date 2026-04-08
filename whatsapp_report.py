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
    print(f"{Fore.RED}Version: 3.1.0  {Fore.GREEN}Mode: Full-Spectrum Long Capture{Style.RESET_ALL}")
    print(f"{Fore.BLUE}[-] Zero-Tolerance Authority Protocols Active {Style.RESET_ALL}\n")

while True:
    show_banner()
    email, password = get_credentials()

    print(f"{Fore.WHITE}[01] BAN PROTOCOL (Full-Length High Priority)")
    print(f"[02] UNBAN PROTOCOL (Legal-Grade Restoration)")
    print(f"[03] EXIT")
    
    main_choice = input(f"\n{Fore.YELLOW}Select Mode: {Fore.WHITE}")

    if main_choice == "01":
        num = input(f"\n{Fore.CYAN}[-] Target Number: {Fore.WHITE}")
        print(f"    [01] Mass Spam [02] Financial Fraud [03] Sexual Spam [04] MALWARE")
        v_choice = input(f"    Choice: {Fore.WHITE}")
        
        v_map = {
            "01": "Coordinated Bulk Spam and Platform Degradation",
            "02": "Organized Financial Fraud and Phishing Operations",
            "03": "Unsolicited Sexual Content and Predator Tactics",
            "04": "Critical Malware and Remote Access Trojan (RAT) Distribution"
        }
        violation = v_map.get(v_choice, "Severe Terms of Service Violations")

        subject = f"ACTION REQUIRED: Cybercrime Complaint & Permanent Ban Request - [{num}]"
        body = f"""To the WhatsApp Trust and Safety / Cybercrime Review Team,

I am submitting this report as a formal cybercrime complaint concerning the WhatsApp account {num}. 

NATURE OF COMPLAINT:
The reported account is involved in coordinated, intentional, and repeated criminal activity categorized as {violation}. This behavior is designed to exploit, deceive, and cause significant harm to the WhatsApp user community.

TECHNICAL DETAILS OF ACTIVITY:
Evidence indicates the account is deploying malicious URLs and social engineering tactics intended to steal personal identification, financial credentials, and account authentication codes. In addition to these fraudulent efforts, the account distributes unsolicited spam content as a lure for hijacking attempts. These tactics are consistent with organized cybercrime operations aimed at undermining platform security and user privacy.

RISK ASSESSMENT:
This account poses an imminent threat to the financial security and safety of the global user base. Furthermore, the distribution of unregulated content represents a specific risk to minors and vulnerable populations on the platform.

REQUEST FOR IMMEDIATE ACTION:
I respectfully request an urgent manual investigation by the Cybercrime Review Team. Given the severity, repetition, and malicious intent identified, I request immediate and permanent account termination to prevent further criminal impact.

Sincerely,
Digital Safety Enforcement Liaison"""

        if send_mail(email, password, num, subject, body):
            print(f"{Fore.GREEN}✅ Full-Spectrum Strike Deployed.{Style.RESET_ALL}")
        
    elif main_choice == "02":
        num = input(f"\n{Fore.CYAN}[-] Recovery Number: {Fore.WHITE}")
        subject = f"FORMAL APPEAL: Wrongful Account Termination Review - {num}"
        body = f"""To the WhatsApp Support & Safety Appeals Board,

I am filing a formal appeal against the suspension of account {num}. 

A thorough internal audit confirms that my account was flagged by an automated algorithmic system in error. I have maintained full compliance with all Terms of Service and have never engaged in unauthorized activity or utilized third-party software. The loss of access to this account is causing irreparable personal and professional damage.

I request an immediate manual human review by a senior supervisor to rectify this false-positive flag and restore my account status immediately.

Respectfully."""
        if send_mail(email, password, num, subject, body):
            print(f"{Fore.GREEN}✅ Legal-Grade Appeal Deployed.{Style.RESET_ALL}")

    elif main_choice == "03": break

    unlock_time = datetime.now() + timedelta(hours=12)
    print(f"\n{Fore.RED}[!] MONITORING ACTIVE. PRESS '0' AND ENTER TO RESET.{Style.RESET_ALL}")
    try:
        while datetime.now() < unlock_time:
            t_str = str(unlock_time - datetime.now()).split('.')[0]
            # \033[K wipes the line to keep UI clean and prevent duplication
            sys.stdout.write(f"\r\033[K{Fore.YELLOW}[COUNTDOWN]: {t_str} {Fore.WHITE}| COMMAND: ")
            sys.stdout.flush()
            ready, _, _ = select.select([sys.stdin], [], [], 1.0)
            if ready:
                if sys.stdin.readline().strip() == "0": break
    except KeyboardInterrupt: break
