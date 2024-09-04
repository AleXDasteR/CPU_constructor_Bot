from selenium import webdriver as wd

path = 'C:/Drivers/chromedriver.exe'

driver = wd.Chrome(executable_path=path)

driver.get('https://www.google.com')

driver.quit()
