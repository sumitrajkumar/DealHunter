from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pywhatkit

def send_email(price):
    # Setup the email parameters
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    password = "your_app_specific_password"   # 2-step verification 
    
    # Create the email content
    subject = "Price Drop Alert!"
    body = f"The price of your tracked product has dropped to ${price}. Check it out now!"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

# Link of your product
website ="https://www.flipkart.com/montrez-full-sleeve-washed-men-jacket/p/itmd7c066190be3b?pid=JCKG5HB9BNRBUSGB&lid=LSTJCKG5HB9BNRBUSGBGXSJIF&marketplace=FLIPKART"
path = "C:\\Users\\sumit\\Videos\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)


price_element = driver.find_element(By.XPATH, '//div[@class="Nx9bqj CxhGGd"]')
price = price_element.text  


price_threshold = 500  # Set your desired price threshold

new_price = price[1:]


price_float = int(new_price)

if price_float < price_threshold:
    print("Price has dropped! Sending email notification.")
    send_email(price)
    print("Price is low.")
else:
    print("Price is still high.")



from datetime import datetime, timedelta

# Get the current time and add 1 minute
current_time = datetime.now()
send_time = current_time + timedelta(minutes=2)

# Extract hour and minute from the updated time
hour = send_time.hour
minute = send_time.minute

# Send the WhatsApp message
pywhatkit.sendwhatmsg("+919693107593", "Price has dropped!", hour, minute, 15, 2)

driver.quit()


