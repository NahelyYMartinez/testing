import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep



class HelloWorld(unittest.TestCase):
    driver: WebDriver = webdriver.Chrome(executable_path="chromedriver.exe")
    @classmethod
    def SetUp(cls):
        driver = cls.driver
        driver.implicitly_wait(10)


    def test1_hello_world(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(3)
        usuario = driver.find_element(By.ID, "user-name")
        usuario.send_keys("standard_user")
        sleep(3)
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        sleep(3)
        button = driver.find_element(By.ID, "login-button")
        button.click()

print("Login correcto")


if __name__ == '__main__':
    print_hi('PyCharm')

