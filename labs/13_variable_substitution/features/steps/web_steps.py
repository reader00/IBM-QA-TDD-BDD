# pylint: disable=function-redefined, missing-function-docstring
# flake8: noqa
"""
Web Steps
Steps file for web interactions with Selenium
For information on Waiting until elements are present in the HTML see:
    https://selenium-python.readthedocs.io/waits.html
"""

from behave import given, when, then


@given('I am on the "Home Page"')
def step_impl(context):
    context.response = context.driver.get(context.base_url)


@when('I set the "Category" to "{category}"')
def step_impl(context, category):
    element = context.driver.find_element_by_id('pet_category')
    element.clear()
    element.send_keys(category)


@when('I click the "Search" button')
def step_impl(context):
    element = context.driver.find_element_by_id('search-btn')
    element.click()


@then('I should see the message "{message}"')
def step_impl(context, message):
    element = context.driver.find_element_by_id('flash_message')
    assert message in element.text


@then('I should see "{pet_name}" in the results')
def step_impl(context, pet_name):
    element = context.driver.find_element_by_id('search_results')
    assert pet_name in element.text


@then('I should not see "{pet_name}" in the results')
def step_impl(context, pet_name):
    element = context.driver.find_element_by_id('search_results')
    assert pet_name not in element.text
