import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

'''
    WebDriver - using selenium python library
    ------------------------------------------
    * Used for accessing web pages via chrome emulation web browser
      and making interactions with html elements/forms

    * chromedriver.exe must reside in the same directory
    
    * Must use webdriver packages containing single chromedriver.exe file
      -> https://googlechromelabs.github.io/chrome-for-testing/#stable
'''

votes = 0
totalVotes = 0
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

while True:
    driver.get('https://biletnikoffaward.com/fan-vote/')
    driver.implicitly_wait(2)

    if driver.find_elements(By.CLASS_NAME, 'gnt_mol_xb'): # locating cover add X
        driver.find_element(By.CLASS_NAME, 'gnt_mol_xb').click() #close cover add
    
    # locate any nested iframes and switch driver to that frame
    # frame = driver.find_element(By.CLASS_NAME, 'gnt_em_pd_if')
    # driver.switch_to.frame(frame)

    if driver.find_element(By.ID, "PDI_answer70813967"):
        # make selection
        button = driver.find_element(By.ID, "PDI_answer70813967")
        button.click()

        # submit form
        submit = driver.find_element(By.ID, "pd-vote-button16081645")
        submit.click()

        time.sleep(2)
        votes += 1
        totalVotes += 1
        print ('submission count: ' + str(totalVotes))

        # reset driver after specific duration
        #  - this helps prevent server blacklisting due to recognized automation
        if votes >= 20:
            driver.quit()
            time.sleep(15)
            service = Service()
            options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(service=service, options=options)
            votes = 0

        #driver.close()   
    else:
        driver.refresh()

