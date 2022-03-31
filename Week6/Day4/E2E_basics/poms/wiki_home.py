from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class WikiHome:

    def __init__(self, driver: WebDriver):
        """by injecting the driver into the POM we make it so the driver can access the necessary elements on the web page"""
        self.driver = driver

    def english(self):
        """this method return the English link so that selenium can interact with it"""
        element: WebElement = self.driver.find_element(By.ID, "js-link-box-en")
        return element
        # return self.driver.find_element(By.ID,"js-link-box-en")

    def spanish(self):
        """for css selector, follow this format: element[attribute='value']"""
        element: WebElement = self.driver.find_element(By.CSS_SELECTOR, "div[lang='es']")
        return element

    def italian(self):
        """you can use xpath or relative xpath"""
        # relative xpath to element: //*[@lang="it"]/a
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/a")
        return element
