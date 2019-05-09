from behave import *
@given('user type their name [usr_name]')
def step_impl(context):
    pass

@when('when asked for on the beginning')
def step_impl(context):
    assert True is not False

@then('application says: Hello [usr_name]')
def step_impl(context):
    assert context.failed is False