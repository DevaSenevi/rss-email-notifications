# 📡 RSS & Email Notification System

## 📌 Overview
This project provides two methods for **automated notifications** when a process completes a task:
1. **RSS Feed Updates** (`hello_rss.py`): Generates an RSS feed every 3 minutes.
2. **Email Alerts** (`hello_email.py`): Sends an email every 3 minutes.

Both scripts run for **20 minutes**, updating every 3 minutes.

---

## 🚀 Setup Instructions

### **1️⃣ Install Dependencies**
Install the required packages using:
'''bash
pip install -r requirements.txt
'''

### **2️⃣ Running the RSS Feed Script**
To generate an RSS feed that updates every 3 minutes:
'''bash
python hello_rss.py
'''

#### **📂 View the RSS Feed**
1. Start a local web server:
'''bash
python3 -m http.server 8000
'''

2. Open your browser and visit:
'''bash
http://localhost:8000/updates.xml
'''

3. If accessing remotely, find your local IP:
'''bash
hostname -I | awk '{print $1}'
'''

4. Then open below in your browser:
'''http://<your-ip>:8000/updates.xml
'''
⚠ Firewall Note: If this is inside a company network, external access may be blocked.

### **3️⃣ Running the Email Notification Script**
To send an email notification every 3 minutes, update hello_email.py with:

- Your Gmail address
- Your App Password (generated via Google App Passwords)
- Recipient's email

Then run:
'''
python hello_email.py
'''

**📌 Make sure to enable 2FA and generate an App Password for Gmail SMTP.
If using another email provider, update the SMTP settings accordingly.**

### **📜 License**
This project is released under the MIT License – You can use, modify, and share freely 😊

