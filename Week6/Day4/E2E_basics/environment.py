from behave.runner import Context
from selenium import webdriver

from poms.wiki_home import WikiHome


def before_all(context: Context):
    # we need to add a driver to the context
    context.driver = webdriver.Chrome("chromedriver.exe")
    # we need to add all poms to the context
    context.wiki_home = WikiHome(context.driver)
    # we need to set an implicit wait for the context
    context.driver.implicitly_wait(1) # this helps prevent "flakey tests"


def after_all(context: Context):
    context.driver.quit()
