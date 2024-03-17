
# 
# Voxstar 15
# Description - Automated Parallel Test Execution - Python Script/Code that shows how to run tests in parallel using Selenium and Python
# Change: Added New Script/Code forAutomated Parallel Test Execution
# Date  : "17.03.2024"
# Version: 1.0 
# More Information : These examples cover a wide range of automation scenarios using Selenium and Python, including automated testing, data entry, 
# job applications, price monitoring, social media interactions, email checking, form filling, survey completion, captcha solving, 
# browser extensions installation, video playback, and file downloads. 
# Further Examples include: examples cover various advanced automation scenarios using Selenium and Python, 
# including web performance testing, visual testing, parallel test execution, browser configuration, web crawling, web application testing, 
# browser fingerprinting, and screenshot stitching

from selenium import webdriver
import unittest
from multiprocessing import Pool

class TestLogin(unittest.TestCase):
    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.example.com/login")

        # Enter login credentials
        username_field = driver.find_element_by_id("username")
        password_field = driver.find_element_by_id("password")
        username_field.send_keys("testuser")
        password_field.send_keys("testpassword")
        password_field.submit()

        # Assert that login was successful
        welcome_message = driver.find_element_by_css_selector(".welcome-message").text
        self.assertEqual(welcome_message, "Welcome, testuser!")

        driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    pool = Pool(processes=4)  # Number of parallel processes
    pool.map(lambda _: unittest.TextTestRunner().run(suite), range(4))
    pool.close()
    pool.join()