# 
# Voxstar 14
# Description - Automated Visual Testing - Python Script/Code that shows how to compare pages using visual testing
# Change: Added New Script/Code for Automated Web Performance Testing
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
from PIL import Image, ImageChops
import os

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Take a screenshot of the current page
driver.save_screenshot("current_page.png")

# Load the expected screenshot
expected_screenshot = Image.open("expected_screenshot.png")
current_screenshot = Image.open("current_page.png")

# Compare the two screenshots
diff = ImageChops.difference(expected_screenshot, current_screenshot)

# Check if there are any visual differences
if diff.getbbox():
    print("Visual differences detected!")
    diff.save("visual_diff.png")
else:
    print("No visual differences found.")

driver.quit()
os.remove("current_page.png")