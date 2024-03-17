# 
# Voxstar 13
# Description - Automated Web Performance Testing - Python Script/Code that shows 
# Change: Added New Script/Code for Automated Web Performance Testing
# Date  : "17.03.2024"
# Version: 1.0 
# More Information : These examples cover a wide range of automation scenarios using Selenium and Python, including automated testing, data entry, 
# job applications, price monitoring, social media interactions, email checking, form filling, survey completion, captcha solving, 
# browser extensions installation, video playback, and file downloads. 
# Further Examples include: examples cover various advanced automation scenarios using Selenium and Python, 
# including web performance testing, visual testing, parallel test execution, browser configuration, web crawling, web application testing, 
# browser fingerprinting, and screenshot stitching

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import statistics

# Set up desired capabilities for performance logging
caps = DesiredCapabilities.CHROME.copy()
caps["goog:loggingPrefs"] = {"performance": "ALL"}

# Initialize the Chrome driver with performance logging enabled
driver = webdriver.Chrome(desired_capabilities=caps)

# Navigate to the website
driver.get("https://www.example.com")

# Collect performance logs
logs = driver.get_log("performance")

# Process the performance logs
navigation_times = []
for log in logs:
    message = log["message"]
    if "Network.requestWillBeSent" in message:
        start_time = log["timestamp"]
    elif "Network.responseReceived" in message:
        end_time = log["timestamp"]
        navigation_times.append(end_time - start_time)

# Calculate performance metrics
navigation_time_mean = statistics.mean(navigation_times)
navigation_time_median = statistics.median(navigation_times)
navigation_time_min = min(navigation_times)
navigation_time_max = max(navigation_times)

# Print the performance metrics
print(f"Mean navigation time: {navigation_time_mean} ms")
print(f"Median navigation time: {navigation_time_median} ms")
print(f"Minimum navigation time: {navigation_time_min} ms")
print(f"Maximum navigation time: {navigation_time_max} ms")

driver.quit()