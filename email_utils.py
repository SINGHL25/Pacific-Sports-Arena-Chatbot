import os
import smtplib
from email.mime.text import MIMEText

def send_booking_email(data):
    try:
        user = os.getenv("EMAIL_USER")
        pwd = os.getenv("EMAIL_PASS")
        to = os.getenv("EMAIL_OWNER")

        message = f"""
New Booking at Pacific Sports Arena:

Name: {data['name']}
Contact: {data['contact']}
Activity: {data['activity']}
Date: {data['date']}
Time: {data['time']}
Feedback: {data['feedback']}
"""

        msg = MIMEText(message)
        msg["Subject"] = "📬 New Booking Notification"
        msg["From"] = user
        msg["To"] = to

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(user, pwd)
            server.send_message(msg)

    except Exception as e:
        print("Email Error:", e)

