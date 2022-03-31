from behave import when, then


@when(u'I enter {criteria} into the search bar')
def step_impl(context, criteria: str):
    raise NotImplementedError(u'STEP: When I enter apple into the search bar')


@when(u'I select {language} as my language option')
def step_impl(context, language: str):
    raise NotImplementedError(u'STEP: When I select en as my language option')


@when(u'I click the search button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the search button')


@then(u'I should be on a page with the title {title}')
def step_impl(context, title: str):
    raise NotImplementedError(u'STEP: Then I should be on a page with the title Apple - Wikipedia')
