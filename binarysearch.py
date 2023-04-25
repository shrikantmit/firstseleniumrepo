# E:\vaibhav tayde\chromedriver_win32
from selenium import webdriver
import time

 
driver = webdriver.Chrome(executable_path="E:\\vaibhav tayde\chromedriver_win32\chromedriver.exe")
driver.get('https://www.facebook.com/')
print(driver.title)
driver.maximize_window()
driver.get('https://www.instagram.com/')
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("abc@123")
time.sleep(3)
driver.quit()
