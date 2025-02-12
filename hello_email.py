###
#Automated Email Notifications
#Sends an email every 3 minutes with "Hello World [i]" updates.
###

import time
import smtplib
from email.message import EmailMessage

# Email Configuration
EMAIL_ADDRESS = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"
TO_EMAIL = "recipient@example.com"

def send_email(update_number):
    msg = EmailMessage()
    msg.set_content(f"Hello World [{update_number}] - Your process updated!")

    msg["Subject"] = "Task Update Alert"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

# Incremental counter
counter = 1
run_time = 20 * 60  # Run for 20 minutes
interval = 3 * 60  # Send email every 3 minutes
start_time = time.time()

while time.time() - start_time < run_time:
    print(f"Sending Email: Hello World [{counter}]")
    send_email(counter)
    counter += 1
    time.sleep(interval)  # Wait 3 minutes before next update
