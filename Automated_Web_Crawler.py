# 
# Voxstar 17
# Description - Parallel Test Execution - Python Script/Code that shows how to setup a Web Crawler and visit a set of URLs 
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
from urllib.parse import urlparse, urljoin
import time

driver = webdriver.Chrome()
start_url = "https://www.example.com"
driver.get(start_url)

# Initialize a set to store visited URLs
visited_urls = set()

# Initialize a queue to store URLs to visit
url_queue = [start_url]

while url_queue:
    current_url = url_queue.pop(0)\
    visited_urls.add(current_url)

    # Extract links from the current page
    links = driver.find_elements_by_tag_name("a")
    for link in links:
        href = link.get_attribute("href")
        if href:
            parsed_href = urlparse(href)
            if parsed_href.netloc == urlparse(start_url).netloc and parsed_href.path not in visited_urls:
                absolute_url = urljoin(start_url, href)
                url_queue.append(absolute_url)

    # Navigate to the next URL
    if url_queue:
        next_url = url_queue[0]
        driver.get(next_url)
        time.sleep(2)  # Wait for the page to load

driver.quit()