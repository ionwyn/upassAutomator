import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# get the path for Chrome Driver
dir = os.path.join(os.path.dirname("C:\\Users\\ionwyn\\Documents\\Python\\Untitled Folder 1\\"))
chrome_driver_path = dir + "\chromedriver.exe"

# Create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
# driver = webdriver.PhantomJS()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to Upass-BC Homepage
driver.get("https://upassbc.translink.ca/")

# Get the University Dropbox
search = Select(driver.find_element_by_id("PsiId"))

# University name
search.select_by_value("sfu")
driver.find_element_by_id("goButton").click()

# Arrived at University Website
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

# Make sure forms are empty
username.clear()
password.clear()

# Input Username and Password
username.send_keys("type_your_username_here")
password.send_keys("type_your_password_here")
password.submit()

#driver.save_screenshot('screen3.png')
driver.find_element_by_id("chk_1").click()
driver.find_element_by_id("requestButton").click()
