from behave import given, when, then
from pages.homePage import HomePage
from utils import utils
from selenium.webdriver.common.by import By

@given('Automation Testing Practice page is displayed')
def step_impl(context):
    context.driver.get(utils.URL)
    context.login_page = HomePage(context.driver)

@when('the user enters valid credentials')
def step_impl(context):
    context.login_page.enter_username(utils.USERNAME)
    context.login_page.enter_email(utils.EMAIL)
    context.login_page.enter_phone(utils.PHONE)
    context.login_page.enter_address(utils.ADDRESS)

@then('the home page should be displayed')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert context.driver.find_element(By.CLASS_NAME, context.home_page.welcome_link_class).is_displayed()