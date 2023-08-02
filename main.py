from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from userInfo import email,password

driver = webdriver.Chrome()
url = "https://accounts.google.com/InteractiveLogin/identifier?elo=1&ifkv=AXo7B7VbT9MoSFRdybnVCxx-lZ-FUO9sR4tj20ErzA295WzNMrdZ3IB0I0EkKQqUzJQ_CDtRL5NS4w&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
driver.get(url)
driver.maximize_window()
time.sleep(3)

emailInput = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
emailInput.click()
emailInput.send_keys(email)

continueInput = driver.find_element(By.XPATH , '//*[@id="identifierNext"]/div/button/span')
continueInput.click()
time.sleep(5)

passwordInput = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
passwordInput.click()
passwordInput.send_keys(password)

continueInput2 = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
continueInput2.click()
time.sleep(2)

url = "https://10fastfingers.com/login"
driver.get(url)
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()

emailInput2 = driver.find_element(By.XPATH, '//*[@id="UserEmail"]')
emailInput2.click()
emailInput2.send_keys(email)

passwordInput2 = driver.find_element(By.XPATH, '//*[@id="UserPassword"]')
passwordInput2.click()
passwordInput2.send_keys(password)

submit = driver.find_element(By.XPATH, '//*[@id="login-form-submit"]')
submit.click()
time.sleep(2)

textInput = driver.find_element(By.XPATH, '//*[@id="inputfield"]')
i = 1
while i < 200:
    textInput.click()
    text = driver.find_element(By.XPATH, '//*[@id="row1"]/span['+str(i)+']').text
    textInput.send_keys(text)
    time.sleep(0.2)
    textInput.send_keys(" ")
    i += 1


