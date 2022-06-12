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
from sys import exit

# Choose Network (ethereum/matic)
network = "matic"

# Enter NFT contract address
contractAddress = "0xc5df71db9055e6e1d9a37a86411fd6189ca2dbbb"

# From which Token ID it should start refreshing?
startFrom = 1753

# Up-to which Token ID it should keep refreshing?
refreshToNumber = 2300


# Run in the background (Headless mode)? True/False
runInBackground = True



# ---------------------------------------- Do not change anything below this comment----------------------------------------------------------

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

options = Options()
options.headless = runInBackground
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')

for tokenId in range(startFrom, refreshToNumber):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    if network.lower() == "matic":
        url = "https://opensea.io/assets/{}/{}/{}".format(network.lower(), contractAddress, tokenId)
    elif network.lower() == "ethereum":
        url = "https://opensea.io/assets/{}/{}/{}".format(network.lower(), contractAddress, tokenId)
    else:
        print(bcolors.WARNING + "ERROR! Wrong network! ONLY ethereum or matic allowed!" + bcolors.ENDC) 
        quit()

    print(bcolors.OKBLUE + "Refreshing NFT #" + str(tokenId) + bcolors.ENDC)
    driver.get(url)
    try:
        try:
            refreshButton = driver.find_element_by_xpath('./html/body/div[1]/div/main/div/div/div/div[2]/div/section[1]/div/div[2]/div/button[1]')
            refreshButton.click()
            print(bcolors.OKGREEN + "SUCCESS - #" + str(tokenId) + bcolors.ENDC)
        except:
            print(bcolors.WARNING + "ERROR! Could not refresh - #" + str(tokenId) + bcolors.ENDC) 
    except:
        print(bcolors.WARNING + "An error has occurred" + bcolors.ENDC)
        time.sleep(1)
        driver.quit()
else:
     print(bcolors.OKGREEN +"Refreshing finished!" + bcolors.ENDC)
