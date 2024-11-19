# DealHunter
A Python-based price tracker that monitors product prices t and sends alerts when prices drop below a specified threshold


---

## Features
- **Automated Price Tracking**: Tracks product prices on Flipkart.
- **Email Notifications**: Sends an email alert when the price drops below the threshold.
- **WhatsApp Alerts**: Sends a WhatsApp message for price alerts.
- **Customizable Threshold**: Set your desired price threshold.

---

## Requirements

### Dependencies
Install the required Python libraries before running the script:

pip install selenium pywhatkit
Additional Setup
ChromeDriver:

Download the appropriate version of ChromeDriver for your system here.
Update the path variable in the script with the location of the ChromeDriver executable.
Gmail Setup:

Enable 2-Step Verification for your Gmail account.
Create an App Password and replace your_app_specific_password in the script with the generated password.
Update sender_email and receiver_email with your email addresses.
WhatsApp:

Ensure the target WhatsApp number is in your contacts.
Replace the number in pywhatkit.sendwhatmsg with the desired recipient's number.
How to Use
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/price-tracker.git
cd price-tracker
Set up dependencies and ChromeDriver.

Replace the placeholders:

Update the Flipkart product URL in the website variable.
Configure email addresses and WhatsApp number.
Run the script:

bash
Copy code
python price_tracker.py
Project Workflow
The script uses Selenium to navigate to the product page and extract the price.
If the price is below the specified threshold:
An email alert is sent using SMTP.
A WhatsApp message is sent using PyWhatKit.
The script runs and exits after checking the price.


Notes
Ensure your network is stable for Selenium and PyWhatKit to function correctly.
Keep ChromeDriver updated to match your Chrome browser version.

