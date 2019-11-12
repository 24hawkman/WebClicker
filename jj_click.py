import sys
import time
from selenium import webdriver

votes = 0
driver = webdriver.Chrome()
driver.get('https://biletnikoffaward.com/fan-vote')


while True:
    #driver = webdriver.Chrome()
    if driver.find_element_by_id('PDI_answer48276570'):
        button = driver.find_element_by_id('PDI_answer48276570')
        button.click()
        submit = driver.find_element_by_id('pd-vote-button10415962')
        submit.click()
        time.sleep(2)
        driver.refresh()
        #driver.close()
        votes += 1
        print (str(votes))
    else:
        driver.refresh()

# initial percentile: 34.45%
