# 
# Voxstar 04
# Description - Automated Price Monitoring - Python Script/Code for Automated Price Monitoring (get current price and send email notification on price change)
# Change: Added New Script/Code for Automated Price Monitoring
# Date  : "17.03.2024"
# Version: 1.0
# More Information : These examples cover a wide range of automation scenarios using Selenium and Python, including automated testing, data entry, 
# job applications, price monitoring, social media interactions, email checking, form filling, survey completion, captcha solving, 
# browser extensions installation, video playback, and file downloads. 
# Further Examples include: examples cover various advanced automation scenarios using Selenium and Python, 
# including web performance testing, visual testing, parallel test execution, browser configuration, web crawling, web application testing, 
# browser fingerprinting, and screenshot stitching
# There are more examples of using Python and Selenium for various automation tasks, including ones that utilizes ChatGPT for code conversion and 
# other examples that incorporate AI in different ways:

from selenium import webdriver
import smtplib

driver = webdriver.Chrome()
driver.get("https://www.example.com/product")

# Get the current price
price = driver.find_element_by_id("product-price").text

# Set a desired price threshold
desired_price = 99.99

# Send an email notification if the price drops below the threshold
if float(price.replace("$", "")) <= desired_price:
    sender = "your_email@example.com"
    receiver = "recipient@example.com"
    subject = "Price Drop Alert"
    body = f"The product price has dropped to {price}!"

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, "your_email_password")
        server.sendmail(sender, receiver, message)

driver.quit()