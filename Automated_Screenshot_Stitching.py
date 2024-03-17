# 
# Voxstar 20
# Description - Automated Screenshot Stitching - Python Script/Code that shows how to take screenshots and stitch them together 
# Change: Added New Script/Code for Automated Screenshot Stitching
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
from PIL import Image
import math

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# Get the dimensions of the viewport and the entire page
viewport_width = driver.execute_script("return document.documentElement.clientWidth")
viewport_height = driver.execute_script("return document.documentElement.clientHeight")
total_width = driver.execute_script("return Math.max(document.body.scrollWidth, document.documentElement.scrollWidth);")
total_height = driver.execute_script("return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);")

# Calculate the number of tiles needed
tiles_x = math.ceil(total_width / viewport_width)
tiles_y = math.ceil(total_height / viewport_height)

# Initialize an empty image to stitch the tiles
stitched_image = Image.new("RGB", (total_width, total_height))

# Capture and stitch the tiles
for y in range(tiles_y):
    for x in range(tiles_x):
        # Scroll to the tile position
        driver.execute_script(f"window.scrollTo({x * viewport_width}, {y * viewport_height});")

        # Capture the tile as a screenshot
        tile_filename = f"tile_{x}_{y}.png"
        driver.save_screenshot(tile_filename)
        tile_image = Image.open(tile_filename)

        # Paste the tile onto the stitched image
        stitched_image.paste(tile_image, (x * viewport_width, y * viewport_height))

        # Clean up the tile screenshot file
        os.remove(tile_filename)

# Save the stitched image
stitched_image.save("stitched_screenshot.png")

driver.quit()