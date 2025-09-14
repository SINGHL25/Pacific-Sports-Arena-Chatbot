# Pacific-Sports-Arena-Chatbot
🏸 Pacific Sports Arena Booking Chatbot
<img width="1024" height="1024" alt="Gemini_Generated_Image_wfkhpowfkhpowfkh" src="https://github.com/user-attachments/assets/96e10985-3379-4917-9ad6-682709ca211a" />

A fully interactive AI-enabled chatbot built with Streamlit, designed to handle bookings, collect customer feedback, and send real-time email alerts to the arena owner.
Ideal for indoor sports complexes, box cricket, badminton courts, event spaces, and commercial shop bookings.

📍 Project Overview
Pacific Sports Arena offers:

7 Badminton Courts (fully furnished)

Box Cricket

Indoor Games

Corporate Event Hosting

Commercial Shops for Lease

This chatbot allows:
✅ Slot Booking
✅ Customer Feedback
✅ Email Notification to Owner
✅ Booking Data Logging to Google Sheets

📁 Folder Structure
graphql
Copy
Edit
pacific_sports_arena_chatbot/
├── app.py                  # Main Streamlit app
├── booking.py              # Google Sheets integration
├── email_utils.py          # Email alert system
├── google-credentials.json # Google Sheet API key (excluded from Git)
├── .env.sample             # Environment variable template
├── requirements.txt        # Required Python packages
├── README.md               # This file
🔧 Features
Feature	Description
✅ Booking Form	Collects name, contact, date, time, activity
📧 Email Alert	Sends confirmation to arena owner
🧾 Google Sheets	Saves bookings to Pacific_Arena_Bookings sheet
🗣 Feedback	Collects additional customer feedback

🚀 Quick Start
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourname/pacific_sports_arena_chatbot.git
cd pacific_sports_arena_chatbot
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Set Up Environment
Create a .env file from the .env.sample:

bash
Copy
Edit
cp .env.sample .env
Fill in your:

EMAIL_USER, EMAIL_PASS

EMAIL_OWNER

4. Set Up Google Sheets Access
Create a service account in Google Cloud

Download the google-credentials.json

Share the Google Sheet with the service email

Rename sheet as Pacific_Arena_Bookings

5. Run the App
bash
Copy
Edit
streamlit run app.py
🛠️ Tech Stack
Streamlit

Google Sheets API (gspread)

Python Email (smtplib, MIME)

dotenv

📷 Screenshots (Optional)
You can add .png files of booking form, success message, and email notification.

📬 Future Add-ons
SMS/WhatsApp alert integration

Admin dashboard for managing bookings

Payment integration (Razorpay or Stripe)

Feedback analytics

👤 Author
Akhilesh Kumar Singh
Email: akhi.singh1989@gmail.com
LinkedIn: Akhilesh Kumar Singh
