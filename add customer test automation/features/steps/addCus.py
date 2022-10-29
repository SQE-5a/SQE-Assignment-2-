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
from selenium.webdriver.support.ui import Select



@given(u'Chrome is launched')
def step_impl(context):
        
        #time.sleep(1)
        context.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver1.exe")
        context.driver.delete_all_cookies()

        #time.sleep(1)
        context.driver.get("https://www.google.com")
        context.driver.maximize_window()      


@given(u'magento url is open')
def step_impl(context):
    context.driver.get("https://magento.kaamkahani.com/admin123/admin/dashboard/index/key/cc37b525545d55a4eaf59b623bb964e855f700687339ada62afede782ebdf7f5/")
    

@when(u'I enter email as "{email}" and password as "{password}"')
def step_impl(context,email,password):
    context.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(email)
    context.driver.find_element(By.XPATH,"//*[@id=\"login\"]").send_keys(password)
    #time.sleep(1)
    

@when(u'I click on signin button')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR,"#login-form > fieldset > div.form-actions > div.actions > button > span").click()
        #time.sleep(1)
        assert True
    except:
        assert False

@then(u'I should be logged in')
def step_impl(context):
    if context.driver.find_element(By.CLASS_NAME,"page-title"):
         assert True
    else:
         assert False


@given(u'I am on dashboard')
def step_impl(context):
    try:
        context.driver.get("https://magento.kaamkahani.com/admin123/admin/dashboard/index/key/cc37b525545d55a4eaf59b623bb964e855f700687339ada62afede782ebdf7f5/")
        context.driver.maximize_window()
        assert True
    except:
        assert False


@when(u'I click on customers logo')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR,'#menu-magento-customer-customer > a').click()
        assert True
        time.sleep(2)
    except:
        assert False


@when(u'I click all customers')
def step_impl(context):
    
    try:
        context.driver.find_element(By.XPATH,'//*[@id="menu-magento-customer-customer"]/div/ul/li[1]/a').click()
        assert True
        time.sleep(3)
    except:
        assert False


@when(u'I click on all add new customer button')
def step_impl(context):
    #
    try:
        context.driver.find_element(By.XPATH,'//*[@id="add"]').click()
        assert True
        time.sleep(3)
    except:
        assert False


@when(u'I select group as "{Wholesale}"')
def step_impl(context,Wholesale):
    try:
        time.sleep(2)
        context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div/div/div[2]/div/div/div[2]/fieldset/fieldset/div/div[1]/div[2]/select").send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER,Keys.RETURN)
        time.sleep(2)
        assert True
    except:
        assert False
    


@when(u'I enter name prefix as "{irt}"')
def step_impl(context,irt):
    try:
        time.sleep(1)
        context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div/div/div[2]/div/div/div[2]/fieldset/div[2]/div[2]/input").send_keys(irt)
        time.sleep(1)
        assert True
    except:
        assert False


@when(u'I enter first name as "{irtaza}"')
def step_impl(context, irtaza):
    try:
        time.sleep(2)
        context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div/div/div[2]/div/div/div[2]/fieldset/div[3]/div[2]/input").send_keys(irtaza)
        time.sleep(1)
        assert True
    except:
        assert False



@when(u'I enter middle name as "{soe}"')
def step_impl(context, soe):
    try:
        time.sleep(2)
        context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div/div/div[2]/div/div/div[2]/fieldset/div[4]/div[2]/input").send_keys(soe)
        time.sleep(1)
        assert True
    except:
        assert False

@when(u'I enter Last name as "{some}"')
def step_impl(context,some):
    try:
        time.sleep(2)
        context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div/div/div[2]/div/div/div[2]/fieldset/div[5]/div[2]/input").send_keys(some)
        time.sleep(1)
        assert True
    except:
        assert False


@when(u'I enter name suffix as "{suffix}"')
def step_impl(context, suffix):
    try:
        time.sleep(2)
        context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div/div/div[2]/div/div/div[2]/fieldset/div[6]/div[2]/input").send_keys(suffix)
        time.sleep(1)
        assert True
    except:
        assert False


@when(u'I enter email as "{email}"')
def step_impl(context,email):
    try:
        time.sleep(2)
        context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div/div/div[2]/div/div/div[2]/fieldset/div[7]/div[2]/input").send_keys(email)
        time.sleep(1)
        assert True
    except:
        assert False


@when(u'I enter DOB as "{date}"')
def step_impl(context,date):
    try:
        time.sleep(2)
        context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div/div/div[2]/div/div/div[2]/fieldset/div[8]/div[2]/input").send_keys(date)
        time.sleep(1)
        assert True
    except:
        assert False


@when(u'I enter tax as "{tax}"')
def step_impl(context,tax):
    try:
        time.sleep(2)
        context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div/div/div[2]/div/div/div[2]/fieldset/div[9]/div[2]/input").send_keys(tax)
        time.sleep(1)
        assert True
    except:
        assert False


@when(u'I select gender as "{gender}"')
def step_impl(context,gender):
    try:
        if gender == "Male":
            context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div/div/div[2]/div/div/div[2]/fieldset/div[10]/div[2]/select").send_keys(Keys.ARROW_DOWN,Keys.ENTER,Keys.RETURN)
        elif gender == "Female":
            context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div/div/div[2]/div/div/div[2]/fieldset/div[10]/div[2]/select").send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER,Keys.RETURN)
        else:
            context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div/div/div[2]/div/div/div[2]/fieldset/div[10]/div[2]/select").send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ARROW_DOWN,Keys.ENTER,Keys.RETURN)
        assert True
    except:
        assert False
        
        
@when(u'I select welcome email as "{Main}"')
def step_impl(context,Main):
    try:
        #context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div[1]/div/div/div[2]/div/div/div[2]/fieldset/div[11]/div[2]/select").send_keys(Keys.ARROW_DOWN,Keys.ENTER,Keys.RETURN)
        assert True
    except:
        assert False
        
    


@when(u'I click on save customer button')
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[1]/div[2]/div/div/button[4]").click()
       
        assert True
    except:
        assert False


@then(u'New customer will be added')
def step_impl(context):
    try:
        time.sleep(2)
        if context.driver.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div/div/div"):
            assert False
        else:
            assert True
         
    except:
        assert False
