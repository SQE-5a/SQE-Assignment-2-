# ---------------------------------------MADE BY IRTAZA-------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm
from behave import* 


@given(u'Chrome is launched')
def step_impl(context):
        
        time.sleep(1)
        context.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver1.exe")
        context.driver.delete_all_cookies()

        time.sleep(1)
        context.driver.get("https://www.google.com")
        context.driver.maximize_window()      


@given(u'magento url is open')
def step_impl(context):
    context.driver.get("https://magento.kaamkahani.com/admin123/admin/dashboard/index/key/cc37b525545d55a4eaf59b623bb964e855f700687339ada62afede782ebdf7f5/")
    

@when(u'I enter email as "{email}" and password as "{password}"')
def step_impl(context,email,password):
    context.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(email)
    context.driver.find_element(By.XPATH,"//*[@id=\"login\"]").send_keys(password)
    time.sleep(1)
    

@when(u'I click on signin button')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR,"#login-form > fieldset > div.form-actions > div.actions > button > span").click()
        time.sleep(1)
        assert True
    except:
        assert False

@then(u'I should be logged in')
def step_impl(context):
    if context.driver.find_element(By.CLASS_NAME,"page-title"):
         assert True
    else:
         assert False

