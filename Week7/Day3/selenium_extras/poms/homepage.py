from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_button(self):
        return self.driver.find_element(By.ID, "button")

    def get_alert(self):
        return self.driver.switch_to.alert

