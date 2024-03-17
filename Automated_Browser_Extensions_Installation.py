# 
# Voxstar 10
# Description - Automated Browser Extensions Installation - Python Script/Code to add path to extension file, add the extension to Chrome
# Change: Added New Script/Code for Automated Browser Extensions Installation
# Date  : "17.03.2024"
# Version: 1.0 
# More Information : These examples cover a wide range of automation scenarios using Selenium and Python, including automated testing, data entry, 
# job applications, price monitoring, social media interactions, email checking, form filling, survey completion, captcha solving, 
# browser extensions installation, video playback, and file downloads. 
# Further Examples include: examples cover various advanced automation scenarios using Selenium and Python, 
# including web performance testing, visual testing, parallel test execution, browser configuration, web crawling, web application testing, 
# browser fingerprinting, and screenshot stitching


from selenium import webdriver
import os

driver = webdriver.Chrome()

# Add the path to the extension file
extension_path = "/path/to/extension.crx"

# Add the extension to Chrome
driver.install_addon(extension_path, temporary=True)

# Navigate to a website
driver.get("https://www.example.com")

# Use the installed extension
# ...

driver.quit()