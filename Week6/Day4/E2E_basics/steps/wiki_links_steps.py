from behave import given, when, then


@given(u'I am on the Wikipedia home page')
def step_impl(context):
    context.driver.get("https://www.wikipedia.org/")


@when(u'I click on the English link')
def step_impl(context):
    context.wiki_home.english().click()


@then(u'I should be on the English Wikipedia main page')
def step_impl(context):
    assert context.driver.title == "Wikipedia, the free encyclopedia"


@when(u'I click on the Spanish link')
def step_impl(context):
    context.wiki_home.spanish().click()


@then(u'I should be on the Spanish Wikipedia main page')
def step_impl(context):
    assert context.driver.title == "Wikipedia, la enciclopedia libre"


@when(u'i click on the Italian link')
def step_impl(context):
    context.wiki_home.italian().click()


@then(u'I should be on the Italian Wikipedia main page')
def step_impl(context):
    assert context.driver.title == "Wikipedia, l'enciclopedia libera"
