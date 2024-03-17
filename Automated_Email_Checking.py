# 
# Voxstar 06
# Description - Automated Email Checking - Python Script/Code that logs into Gmail and prints the subjects of the emails in the inbox
# Change: Added New Script/Code for Automated Form Filling
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
import time

driver = webdriver.Chrome()
driver.get("https://www.gmail.com")

# Login to Gmail
username_field = driver.find_element_by_id("identifierId")
username_field.send_keys("your_email@gmail.com")
username_field.send_keys(Keys.RETURN)
time.sleep(2)

password_field = driver.find_element_by_name("password")
password_field.send_keys("your_password")
password_field.send_keys(Keys.RETURN)

# Wait for the inbox to load
time.sleep(5)

# Get a list of email subjects
email_subjects = driver.find_elements_by_css_selector(".subject span")
for subject in email_subjects:
    print(subject.text)

driver.quit()