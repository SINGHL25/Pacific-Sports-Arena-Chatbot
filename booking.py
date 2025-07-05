import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def save_booking_to_sheet(data):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("google-credentials.json", scope)
        client = gspread.authorize(creds)
        
        sheet = client.open("Pacific_Arena_Bookings").sheet1
        sheet.append_row([
            data["name"], data["contact"], data["activity"],
            data["date"], data["time"], data["feedback"]
        ])
    except Exception as e:
        print("Google Sheet Error:", e)

