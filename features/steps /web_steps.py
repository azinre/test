from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@when('I click the "{button_name}" button')
def step_impl(context, button_name):
    button = context.browser.find_element(By.NAME, button_name)
    button.click()
    
@then('I should see the text "{text}"')
def step_impl(context, text):
    body = context.browser.find_element(By.TAG_NAME, 'body')
    assert text in body.text, f'Expected text "{text}" not found!'
    
@then('I should not see the text "{text}"')
def step_impl(context, text):
    body = context.browser.find_element(By.TAG_NAME, 'body')
    assert text in body.text, f'Found unexpected text "{text}"'
    
@then('I should see the message "{message}"')
def step_impl(context, message):
    alert = context.browser.find_element(By.CLASS_NAME, 'alert')
    assert message in alert.text, f'Expected message "{message}" not found in alert'