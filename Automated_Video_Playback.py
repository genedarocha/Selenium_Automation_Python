# 
# Voxstar 
# Description - Automated File Downloads - Python Script/Code that shows how to setup File Downloads
# Change: Added New Script/Code for Automated File Downloads
# Date  : "17.03.2024"
# 
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