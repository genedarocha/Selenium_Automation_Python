# 
# Voxstar 19
# Description - Automated Browser FingerPrinting - Python Script/Code that shows how to perform browser fingerprinting using Selenium and Python 
#               ,Navigate to the website and collect browser fingerprints
# Change: Added New Script/Code for Automated Browser FingerPrinting
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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Set up desired capabilities for browser fingerprinting
caps = DesiredCapabilities.CHROME.copy()
caps["goog:chromeOptions"] = {
    "args": [
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "--disable-gpu",
        "--disable-extensions",
        "--proxy-server='direct://'",
        "--proxy-bypass-list=*",
        "--start-maximized",
        "--incognito"
    ]
}

# Initialize the Chrome driver with desired capabilities
driver = webdriver.Chrome(desired_capabilities=caps)

# Navigate to the website and collect browser fingerprints
driver.get("https://www.example.com")
user_agent = driver.execute_script("return navigator.userAgent;")
webgl_renderer = driver.execute_script("return WebGLRenderingContext.prototype.getParameter(WebGLRenderingContext.RENDERER);")
plugin_list = driver.execute_script("return navigator.plugins.length;")
timezone = driver.execute_script("return Intl.DateTimeFormat().resolvedOptions().timeZone;")

# Print the collected fingerprints
print(f"User Agent: {user_agent}")
print(f"WebGL Renderer: {webgl_renderer}")
print(f"Number of Plugins: {plugin_list}")
print(f"Time Zone: {timezone}")

driver.quit()