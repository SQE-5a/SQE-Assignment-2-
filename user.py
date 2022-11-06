import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from behave import*
from selenium.webdriver.support.ui import Select



@given(u'Chrome is launched')
def step_impl(context):
    context.driver = webdriver.Chrome("D:\Driver\chromedriver.exe")
    context.driver.delete_all_cookies()

    # time.sleep(1)
    context.driver.get("https://www.google.com")
    context.driver.maximize_window()

@given(u'I am on my account')
def step_impl(context):
    context.driver.get("https://magento.jsmartfix.com/")


@when(u'I click on whats new')
def step_impl(context):
    try:
      context.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/nav/ul/li[1]/a").click()
      assert True
    except:
      assert False


@when(u'I click on jackets')
def step_impl(context):
    try:
     context.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[4]/div[2]/div/div/ul[2]/li[2]/a").click()
     time.sleep(2)
     assert True
    except:
      assert  False

@when(u'I choose the jacket')
def step_impl(context):
    try:
      context.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[3]/div[1]/div[3]/ol/li[1]/div/a/span/span/img").click()
      time.sleep(2)
      assert True
    except:
        assert False

@when(u'I select size')
def step_impl(context):
    try:
      context.driver.find_element(By.CSS_SELECTOR, "#option-label-size-143-item-166").click()
      time.sleep(1)
      assert True
    except:
        assert False




@when(u'I select color')
def step_impl(context):
    try:
     context.driver.find_element(By.CSS_SELECTOR, "#option-label-color-93-item-49").click()
     time.sleep(2)
     assert True
    except:
        assert False


@when(u'I click add to cart')
def step_impl(context):
    try:
     context.driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div[1]/div[4]/form/div[2]/div/div/div[2]/button").click()
     time.sleep(11)
     assert True
    except:
        assert False



@then(u'Product will get added')
def step_impl(context):
    try:
     context.driver.find_element(By.CSS_SELECTOR, "body > div.page-wrapper > header > div.header.content > div.minicart-wrapper > a").click()
     time.sleep(4)
     assert True
    except:
        assert False


