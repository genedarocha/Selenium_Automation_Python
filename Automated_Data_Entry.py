# 
# Voxstar 02
# Description - Automated Data Entry - Python Script/Code that loads data from a CSV file and enters it into a form
# Change: Added New Script/Code for Automated Data Entry
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
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.example.com/data-entry")

# Load data from a CSV file
data = pd.read_csv("data.csv")

# Iterate through the data and enter it into a form
for index, row in data.iterrows():
    name_field = driver.find_element_by_id("name")
    email_field = driver.find_element_by_id("email")
    phone_field = driver.find_element_by_id("phone")

    name_field.send_keys(row["name"])
    email_field.send_keys(row["email"])
    phone_field.send_keys(row["phone"])

    submit_button = driver.find_element_by_id("submit")
    submit_button.click()

driver.quit()