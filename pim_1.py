from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s= Service("C:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#click PIM Module
driver.find_element(By.XPATH,"//span[text()='PIM']").click()
#click Add
driver.find_element(By.XPATH,"//button[text()=' Add ']").click()
#Add png photo
time.sleep(3)
#photo=driver.find_element(By.XPATH,"//button[@class='oxd-icon-button employee-image-action']")
#photo.send_keys("C:/Users/ELCOT/Desktop.sam.png")
#First name
first=driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
first.send_keys("James")
#Middle name
middle=driver.find_element(By.XPATH,"//input[@placeholder='Middle Name']")
middle.send_keys("Anand")
#Last name
last=driver.find_element(By.XPATH,"//input[@placeholder='Last Name']")
last.send_keys("Innocent")
#click
driver.find_element(By.XPATH,"//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
#username
user=driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")
user.send_keys("jamesanand333")
#password
password=driver.find_element(By.XPATH,"(//input[@type='password'])[1]")
password.send_keys("James@333")
#confirm
confirm=driver.find_element(By.XPATH,"(//input[@type='password'])[2]")
confirm.send_keys("James@333")
#save
save=driver.find_element(By.XPATH,"//button[text()=' Save ']").click()

