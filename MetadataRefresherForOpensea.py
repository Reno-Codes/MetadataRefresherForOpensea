'''
By: Renato Lulic
Instagram: renato_lulic
Date: June 12th, 2022

For instructions or information, please refer to https://github.com/renolulic94/MetadataRefresherForOpensea/blob/master/README.md
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# To wait for side load
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Allows us to use keyboard keys
from selenium.webdriver.common.keys import Keys
import time

# NFT contract address
contractAddress = "0xc5df71db9055e6e1d9a37a86411fd6189ca2dbbb"

# From which Token ID it should start refreshing?
startFrom = 1528

# Up-to which Token ID it should keep refreshing?
refreshToNumber = 2300


# Run in the background (Headless mode)? True/False
runInBackground = False



# ---------------------------------------- Do not change anything below this comment----------------------------------------------------------
options = Options()
options.headless = runInBackground
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')

for tokenId in range(startFrom, refreshToNumber):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    url = "https://opensea.io/assets/matic/{}/{}".format(contractAddress, tokenId)
    driver.get(url)
    try:
        try:
            refreshButton = driver.find_element_by_xpath('./html/body/div[1]/div/main/div/div/div/div[2]/div/section[1]/div/div[2]/div/button[1]')
            refreshButton.click()
            print("SUCCESS! Refreshing")
        except:
            print("ERROR! Could not refresh!")
    except:
        print("An error has occurred")
        time.sleep(1)
        driver.quit()
else:
     print("Refreshing finished!")