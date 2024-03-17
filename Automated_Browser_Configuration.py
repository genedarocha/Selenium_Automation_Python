# 
# Voxstar 16
# Description - Automated Browser Configuration - Python Script/Code shows how to configure the browser for automated testing
# Change: Added New Script/Code for  Automated Browser Configuration
# Date  : "17.03.2024"
# Version: 1.0 
# More Information : These examples cover a wide range of automation scenarios using Selenium and Python, including automated testing, data entry, 
# job applications, price monitoring, social media interactions, email checking, form filling, survey completion, captcha solving, 
# browser extensions installation, video playback, and file downloads. 
# Further Examples include: examples cover various advanced automation scenarios using Selenium and Python, 
# including web performance testing, visual testing, parallel test execution, browser configuration, web crawling, web application testing, 
# browser fingerprinting, and screenshot stitching

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Start Chrome maximized
chrome_options.add_argument("--incognito")  # Open in incognito mode
chrome_options.add_argument("--disable-extensions")  # Disable extensions
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")  # Set a custom user agent

# Set up desired capabilities
caps = webdriver.DesiredCapabilities.CHROME.copy()
caps["goog:loggingPrefs"] = {"performance": "ALL"}  # Enable performance logging

# Initialize the Chrome driver with options and capabilities
driver = webdriver.Chrome(options=chrome_options, desired_capabilities=caps)

# Navigate to the website
driver.get("https://www.example.com")

# Perform actions
# ...

driver.quit()