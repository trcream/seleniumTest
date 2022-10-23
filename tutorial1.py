# Package Installer Python 

# Step 1: pip3 install selenium

# Step 2: download Chrome Driver

# The webdriver is driving all of our interactions with the browser 
from selenium import webdriver
# Fixing the deprecrated warning
from selenium.webdriver.chrome.service import Service
# Access to things like the enter and escape keys 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



s = Service("/usr/local/bin/chromedriver")
# Loading the driver to the browser that we want to use 
driver =  webdriver.Chrome(service=s)

#Opening the browser
driver.get("https://www.techwithtim.net/")
# driver.get("https://opensea.io/collection/decentraland")

print(driver.title)

# ID -> Name - > Class priority or by value
# Finding the search field
search = driver.find_element(By.NAME, "s")
# Entering test
search.send_keys("Trenton is cool")
# Hitting enter to return the results 
search.send_keys(Keys.RETURN)

#driver.quit()
# <input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" type="text" aria-autocomplete="both"
#  aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" 
#  spellcheck="false" title="Search" value="" aria-label="Search" data-ved="0ahUKEwjIo_nKx_X6AhVkHTQIHet2Bh0Q39UDCAY">