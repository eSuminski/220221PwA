from behave import given, when, then
from selenium.webdriver.support.expected_conditions import alert_is_present, invisibility_of_element
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I am on the homepage')
def step_impl(context):
    context.driver.get("C:/Users/EricSuminski/Desktop/220221PwA/Week7/Day3/delay-disappear.html")


@when(u'I click the button')
def step_impl(context):
    context.homepage.get_button().click()


@then(u'I should be able to read an alert with some text in it')
def step_impl(context):
    WebDriverWait(context.driver,4).until(alert_is_present())
    assert context.homepage.get_alert().text == "this shows up after 3 seconds!"


@then(u'I should no longer be able to see the button')
def step_impl(context):
    context.homepage.get_alert().accept()
    WebDriverWait(context.driver,1).until(invisibility_of_element(context.homepage.get_button()),message="buton is still there!")
