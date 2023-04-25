from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="E:\\vaibhav tayde\chromedriver_win32\chromedriver.exe")

driver.get('https://www.google.com/intl/en-GB/gmail/about/')
time.sleep(3)

driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div/div/div/div[3]/div[1]/a/span[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,'')



