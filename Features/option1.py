from behave import *
@given('User choose option 1')
def step_impl(context):
    pass

@when('Asked what to do')
def step_impl(context):
    assert True is not False

@then('Next action takes place')
def step_impl(context):
    assert context.failed is False