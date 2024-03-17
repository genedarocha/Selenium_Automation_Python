# 
# Voxstar 
# Description - Automated File Downloads - Python Script/Code that shows how to setup File Downloads
# Change: Added New Script/Code for Automated File Downloads
# Date  : "17.03.2024"
# 

from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.get("https://www.example.com/files")

# Click on a file download link
download_link = driver.find_element_by_link_text("Download File")
download_link.click()

# Wait for the file to download
driver.implicitly_wait(10)  # Adjust the wait time as needed

# Move the downloaded file to a desired location
downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
downloaded_file = os.path.join(downloads_dir, "file.zip")
new_location = "/path/to/desired/location/file.zip"
os.rename(downloaded_file, new_location)

driver.quit()