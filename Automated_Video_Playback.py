# 
# Voxstar 11
# Description - Automated Video Playback - Python Script/Code searches for a video, click on the first search result and wait for video to load
# Change: Added New Script/Code for Automated Video Playback
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
driver.get("https://www.youtube.com")

# Search for a video
search_box = driver.find_element_by_name("search_query")
search_box.send_keys("tutorial video")
search_box.send_keys(Keys.RETURN)

# Click on the first search result
search_results = driver.find_elements_by_id("video-title")
search_results[0].click()

# Wait for the video to load
time.sleep(5)

# Play the video
video_player = driver.find_element_by_tag_name("video")
video_player.send_keys("k")  # Press the 'k' key to play/pause

# Adjust playback speed
video_player.send_keys(">")  # Press the '>' key to increase playback speed

driver.quit()