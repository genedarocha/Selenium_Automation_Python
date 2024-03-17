# 
# Voxstar 09
# Description - Automated Captcha Solving - Python Script/Code that loads captcha image, saves captcha image to file and uses Pytesseract to extract text 
# Change: Added New Script/Code for Automated Captcha Solving
# Date  : "17.03.2024"
# Version: 1.0 
# More Information : These examples cover a wide range of automation scenarios using Selenium and Python, including automated testing, data entry, 
# job applications, price monitoring, social media interactions, email checking, form filling, survey completion, captcha solving, 
# browser extensions installation, video playback, and file downloads. 
# Further Examples include: examples cover various advanced automation scenarios using Selenium and Python, 
# including web performance testing, visual testing, parallel test execution, browser configuration, web crawling, web application testing, 
# browser fingerprinting, and screenshot stitching


from selenium import webdriver
import time
from PIL import Image
import pytesseract

driver = webdriver.Chrome()
driver.get("https://www.example.com/captcha")

# Locate the captcha image
captcha_image = driver.find_element_by_id("captcha-image")

# Save the captcha image to a file
captcha_image.screenshot("captcha.png")

# Use Pytesseract to extract text from the captcha image
captcha_text = pytesseract.image_to_string(Image.open("captcha.png"))

# Enter the captcha text and submit the form
captcha_field = driver.find_element_by_id("captcha")
captcha_field.send_keys(captcha_text)
submit_button = driver.find_element_by_id("submit")
submit_button.click()

driver.quit()