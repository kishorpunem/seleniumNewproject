import time

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
path = "C:\\Users\\Kishor\\Downloads\\edgedriver_win64 (1)\\msedgedriver.exe"
driver = Edge(executable_path=path)
driver.get("http://test.trukker.ae/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID, "btnLoginLink").click()
driver.find_element(By.ID, "user_id").send_keys("srivani.koneti@trukker.com")
driver.find_element(By.ID, "password").send_keys("123")
driver.find_element(By.ID, "btnLogin").click()
driver.implicitly_wait(50)
driver.find_element(By.XPATH,"//span[contains(text(),'Inquiry')]").click()
print(driver.title)
driver.implicitly_wait(50)
driver.find_element(By.XPATH,"//button[contains(.,'Add New')]").click()

