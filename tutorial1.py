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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
search.send_keys("test")
# Hitting enter to return the results 
search.send_keys(Keys.RETURN)

# waiting before we move on to the next part of our script
try:
    # waiting a max of 10 seconds
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    print("test")
    # Find all of the articles
    # print(main.text)
    articles =  main.find_elements(by = By.TAG_NAME, value = "article")
    print(articles)
    for article in articles:
        header = article.find_element(by=By.CLASS_NAME,value="entry-summary")
        print(header.text)
    # Only quit if it doesn't load properly
finally:
    driver.quit()



# Scraping the full website  
#print(driver.page_source)

#driver.quit()
