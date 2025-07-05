import streamlit as st
import datetime
import os
import smtplib
from email.mime.text import MIMEText

st.set_page_config(page_title="Pacific Sports Arena Chatbot", layout="centered")
st.title("🏸 Pacific Sports Arena Chatbot")
st.markdown("""
Welcome to **Pacific Sports Arena** in Hinjewadi Phase 1! We offer:

- 🏸 7 Badminton Courts (Fully Furnished)
- 🏏 Box Cricket
- 🎯 Indoor Games
- 🏢 Commercial Shops for Lease
- 👔 Corporate Event Bookings
""")

with st.form("booking_form"):
    st.subheader("📅 Book a Slot")
    name = st.text_input("Your Name")
    contact = st.text_input("Contact Number or Email")
    activity = st.selectbox("Choose Activity", ["Badminton", "Box Cricket", "Indoor Games", "Corporate Event"])
    date = st.date_input("Booking Date", datetime.date.today())
    time = st.time_input("Preferred Time Slot")
    submitted = st.form_submit_button("Submit Booking")

    if submitted:
        st.success("✅ Booking submitted successfully!")

        # Compose email
        msg = MIMEText(f"""
New Booking Request:

Name: {name}
Contact: {contact}
Activity: {activity}
Date: {date}
Time: {time}
""")
        msg["Subject"] = "📬 New Booking - Pacific Sports Arena"
        msg["From"] = os.getenv("EMAIL_USER", "your-email@gmail.com")
        msg["To"] = os.getenv("EMAIL_OWNER", "owner@example.com")

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
                server.send_message(msg)
        except Exception as e:
            st.error("⚠️ Email notification failed. Check SMTP credentials in .env.")

