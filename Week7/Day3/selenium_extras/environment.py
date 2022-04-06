from selenium import webdriver
from behave.runner import Context

from poms.homepage import Homepage


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.homepage = Homepage(context.driver)
    context.driver.implicitly_wait(1)


def after_all(context: Context):
    context.driver.quit()
