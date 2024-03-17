# 
# Voxstar 03
# Description - Automated Job Applications - Python Script/Code for Automated Job Applications , fill out job application form , submit the application and check for a successful submission message
# Change: Added New Script/Code for 
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
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Open job application form
driver.get("https://www.example.com/jobs/apply")

# Fill out the application form
name_field = driver.find_element_by_id("name")
email_field = driver.find_element_by_id("email")
resume_upload = driver.find_element_by_id("resume-upload")

name_field.send_keys("John Doe")
email_field.send_keys("john@example.com")
resume_upload.send_keys("/path/to/resume.pdf")

# Submit the application
submit_button = driver.find_element_by_id("submit")
submit_button.click()

# Wait for the confirmation page to load
time.sleep(5)

# Check for a successful submission message
success_message = driver.find_element_by_css_selector(".success-message").text
assert "Application submitted successfully" in success_message

driver.quit()