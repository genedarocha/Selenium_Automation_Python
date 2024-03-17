# 
# Voxstar 18
# Description - Automated Web Application Testing - Python Script/Code that shows how to configure the browser for automated testing 
#               and perform various browser configurations using Selenium and Python   
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
import unittest

class TestApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example.com/app")

    def test_login(self):
        # Test the login functionality
        username_field = self.driver.find_element_by_id("username")
        password_field = self.driver.find_element_by_id("password")
        username_field.send_keys("testuser")
        password_field.send_keys("testpassword")
        password_field.submit()

        # Assert that login was successful
        welcome_message = self.driver.find_element_by_css_selector(".welcome-message").text
        self.assertEqual(welcome_message, "Welcome, testuser!")

    def test_create_item(self):
        # Test the functionality to create a new item
        self.driver.find_element_by_link_text("Create Item").click()
        item_name_field = self.driver.find_element_by_id("item-name")
        item_name_field.send_keys("New Item")
        self.driver.find_element_by_id("submit").click()

        # Assert that the item was created successfully
        item_list = self.driver.find_elements_by_css_selector(".item-list li")
        self.assertIn("New Item", [item.text for item in item_list])

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()