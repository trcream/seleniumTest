# Package Installer Python 

# Step 1: pip3 install selenium

# Step 2: download Chrome Driver

# The webdriver is driving all of our interactions with the browser 
from selenium import webdriver
# Fixing the deprecrated warning
from selenium.webdriver.chrome.service import Service


s = Service("/usr/local/bin/chromedriver")
# Loading the driver to the browser that we want to use 
driver =  webdriver.Chrome(service=s)

driver.get("https://opensea.io/collection/decentraland")

