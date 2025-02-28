# Dynamic-Flight-Ticket-Price-Monitor
# OverView
This project automates the tracking of ticket prices for a specified route (e.g., City A → City B) using an online ticket API. The system sends alerts via email (SMTP) and SMS (Twilio) when the price drops below a predefined threshold.

# Tech Stack
  Programming Language: Python
  APIs: Public Ticket API
  Messaging Services: Twilio API (SMS), SMTP (Email)
  Automation: Python Scheduling

# Project Workflow
  📌 Fetch Ticket Prices: The script calls a free online API to check current ticket prices.
  📌 Compare Against Threshold: If the price drops below a set amount, an alert is triggered.
  📌 Send Notifications: Users receive an SMS (via Twilio) and an email (via SMTP) notifying them of the price drop.

# Features
  ✔️ Real-time tracking of ticket prices
  ✔️ Automated alerts via email & SMS
  ✔️ Customizable price threshold

# Future Enhancements 🚀
  Support for multiple routes
  Integration with Telegram/WhatsApp bots
