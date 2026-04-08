# 🛡️ Disclaimer
​This tool is for educational and authorized security testing purposes only. The developers of ANON-Tactical are not responsible for any misuse or violations of third-party Terms of Service.

# 🛡️ ANON-Tactical v2.6.0
**Elite Strike & Recovery Hybrid Protocol**

ANON  is a specialized Python-based interface designed for high-impact security reporting and account restoration appeals. It utilizes professional-grade "Authority Tone" evidence to ensure reports are prioritized by safety teams.

---
#  App password Guide
​How to generate your SMTP Key:
​Enable 2FA: Go to your Google Account Security settings and ensure 2-Step Verification is turned ON.
​Search for App Passwords: In the search bar at the top of your Google Account, type "App passwords".
​Create Name: Give it a name of your choice
​Copy the Code: Google will show you a 16-character code (e.g., abcd efgh ijkl mnop).
​Paste into ANON: When the script asks for your password, paste that 16-digit code.

## 🚀 Quick Start (Termux/Linux)

To deploy the protocol on a fresh environment, run the following commands:

```bash
# Update and Install Dependencies
pkg update && pkg upgrade -y
pkg install python git -y
pip install colorama requests

# Clone the Repository
git clone [https://github.com/destinyjob2007-gif/whatsapp_report.git](https://github.com/destinyjob2007-gif/whatsapp_report.git)
cd whatsapp_report

# Launch the Interface
python whatsapp_report.py
