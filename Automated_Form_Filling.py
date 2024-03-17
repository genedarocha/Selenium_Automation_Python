# 
# Voxstar 07
# Description - Automated Form Filling - Python Script/Code Fils out the registration form with fake data 
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
from faker import Faker

driver = webdriver.Chrome()
driver.get("https://www.example.com/register")

fake = Faker()

# Fill out the registration form with fake data
name_field = driver.find_element_by_id("name")
email_field = driver.find_element_by_id("email")
password_field = driver.find_element_by_id("password")

name_field.send_keys(fake.name())
email_field.send_keys(fake.email())
password_field.send_keys(fake.password())

submit_button = driver.find_element_by_id("submit")
submit_button.click()

driver.quit()