import time

from selenium.webdriver.support.ui import Select

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\PC\Downloads\chromedriver_win32 (4)\Chromedriver.exe")
driver.get("http://mitintech.com/admin/login/?next=/admin/")
time.sleep(3)
driver.find_element(By.NAME,'username').send_keys('SHRIKANTWANJARI')
time.sleep(2)
driver.find_element(By.NAME,'password').send_keys('SHRIKANT.15')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="login-form"]/div[3]/input').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="content-main"]/div[2]/table/tbody/tr[4]/th/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[4]/td/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="content"]/h1')
driver.find_element(By.NAME,'name').send_keys('BIOLOGY')
time.sleep(2)
driver.find_element(By.NAME,'description').send_keys('biology is an important subject in medical fiel')
time.sleep(2)
driver.find_element(By.NAME,'_save').click()
time.sleep(2)
driver.find_element(By.NAME,'_addanother').click()
time.sleep(2)
driver.find_element(By.NAME,'_continue').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[1]/th/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[1]/td/a').click()
time.sleep(2)
selsub=Select(driver.find_element(By.XPATH,'//*[@id="id_subject"]'))
selsub.select_by_index(14)
driver.find_element(By.NAME,'subject').click()
time.sleep(2)
driver.find_element(By.NAME,'name').send_keys('shrikant')
time.sleep(2)
driver.find_element(By.NAME,'_save').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[3]/th').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[3]/td/a').click()
time.sleep(2)
driver.find_element(By.NAME,'name').send_keys('MBBS')
time.sleep(2)
driver.find_element(By.NAME,'_save').send_keys()
time.sleep(2)
driver.find_element(By.NAME,'_addanother').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[2]/th/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[2]/table/tbody/tr[2]/td/a').click()
time.sleep(2)
driver.find_element(By.NAME,'name').send_keys('SHRIKANT')
time.sleep(2)
selsub=Select(driver.find_element(By.NAME,'subject'))
selsub.select_by_index(14)
time.sleep(2)
selsub=Select(driver.find_element(By.NAME,'bookseries'))
selsub.select_by_index(12)
time.sleep(2)
selsub=Select(driver.find_element(By.NAME,'classid'))
selsub.select_by_index(8)
time.sleep(2)
driver.find_element(By.NAME,'_save').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[3]/table/tbody/tr[3]/th/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[3]/table/tbody/tr[3]/td/a').click()
time.sleep(2)
selsub=Select(driver.find_element(By.ID,'id_subject'))
selsub.select_by_index(14)
time.sleep(2)
selsub=Select(driver.find_element(By.ID,'id_bookseries'))
selsub.select_by_index(14)
time.sleep(2)
selsub=Select(driver.find_element(By.ID,'id_classid'))
selsub.select_by_index(8)
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="id_lesson"]').send_keys("C:\\Users\\PC\\Downloads\\Selenium automation notes mit (2).pdf")
time.sleep(2)
driver.find_element(By.NAME,'_save')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[3]/table/tbody/tr[4]/td/a').click()
time.sleep(2)
selsub=Select(driver.find_element(By.NAME,'subject'))
selsub.select_by_index(14)
time.sleep(2)
selsub=Select(driver.find_element(By.NAME,'bookseries'))
selsub.select_by_index(13)
time.sleep(2)
selsub=Select(driver.find_element(By.NAME,'classid'))
selsub.select_by_index(8)
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="id_solution"]').send_keys("C:\\Users\\PC\\Downloads\\Selenium automation notes mit (2).pdf")
time.sleep(2)
driver.find_element(By.NAME,'_save').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[3]/table/tbody/tr[9]/td/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="content"]/h1')
time.sleep(2)
driver.find_element(By.NAME,'worksheet1').send_keys("C:\\Users\\PC\\Downloads\\Selenium automation notes mit (2).pdf")
time.sleep(2)
driver.find_element(By.NAME,'worksheet2').send_keys("C:\\Users\\PC\\Downloads\\Selenium automation notes mit (2).pdf")
time.sleep(2)
selsub=Select(driver.find_element(By.NAME,'subject'))
selsub.select_by_index(14)
time.sleep(2)
selsub=Select(driver.find_element(By.NAME,'bookseries'))
selsub.select_by_index(5)
selsub=Select(driver.find_element(By.NAME,'classid'))
selsub.select_by_index(8)
time.sleep(2)
selsub=Select(driver.find_element(By.NAME,'chapter'))
selsub.select_by_index(4)
time.sleep(2)
driver.find_element(By.NAME,'_save').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-sidebar"]/div[3]/table/tbody/tr[8]/td/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="content"]/h1')
time.sleep(2)
selsub=Select(driver.find_element(By.NAME,'user'))
selsub.select_by_index(3)
driver.find_element(By.NAME,'schools').send_keys('shri umyia shankar school')
selsub=Select(driver.find_element(By.NAME,'subject'))
selsub.select_by_index(7)
selsub=Select(driver.find_element(By.NAME,'bookseries'))
selsub.select_by_index(4)
selsub=Select(driver.find_element(By.NAME,'state'))
selsub.select_by_index(1)
selsub=Select(driver.find_element(By.NAME,'city'))
selsub.select_by_index(1)
driver.find_element(By.NAME,'mobile').send_keys('8459873444')
time.sleep(1)
driver.find_element(By.NAME,'status').click()
time.sleep(3)
driver.find_element(By.NAME,'_save').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="content-main"]/div[3]/table/tbody/tr[7]/td[1]/a')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="content"]/h1').click()
selsub=Select(driver.find_element(By.NAME,'subject'))
selsub.select_by_index(7)
selsub=Select(driver.find_element(By.NAME,'bookseries'))
selsub.select_by_index(3)
selsub=Select(driver.find_element(By.NAME,'classid'))
selsub.select_by_index(5)
driver.find_element(By.NAME,'viewbook').send_keys("C:\\Users\\PC\\Downloads\\Selenium automation notes mit (2).pdf")
driver.find_element(By.NAME,'_save').click()
time.sleep(2)












