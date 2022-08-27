import time

import pytest
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By


@pytest.fixture()
def setPath():
    global driver
    path = "C:\\Users\\Kishor\\Downloads\\edgedriver_win64 (1)\\msedgedriver.exe"
    driver = Edge(executable_path=path)
    yield
    driver.close()


# a = 101


# @pytest.mark.skip(a > 100, reason="Dont want to execute current build")
# @pytest.mark.Smoke
def test_Logintotheapplication(setPath):
    driver.get("http://test.trukker.ae/")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.ID, "btnLoginLink").click()
    driver.find_element(By.ID, "user_id").send_keys("srivani.koneti@trukker.com")
    driver.find_element(By.ID, "password").send_keys("123")
    driver.find_element(By.ID, "btnLogin").click()
    driver.get_screenshot_as_file("C:/Users/Kishor/PycharmProjects/TestCasesDesign/Afterlogin.png")
    #assert driver.title("TruKKer Login Page")


# @pytest.mark.Sanity
def test_LogintothInvalideapplication(setPath):
    driver.get("http://test.trukker.ae/")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.ID, "btnLoginLink").click()
    driver.find_element(By.ID, "user_id").send_keys("srivani.koneti@trukker.com")
    driver.find_element(By.ID, "password").send_keys("123")
    driver.find_element(By.ID, "btnLogin").click()
    #assert driver.current_url("http://test.trukker.ae/")


# @pytest.mark.Smoke
def test_Logintothe(setPath):
    driver.get("http://test.trukker.ae/")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.ID, "btnLoginLink").click()
    driver.find_element(By.ID, "user_id").send_keys("srivani.koneti@trukker.com")
    driver.find_element(By.ID, "password").send_keys("123")
    driver.find_element(By.ID, "btnLogin").click()
