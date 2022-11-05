import html
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from behave import*

@given(u'chrome is opened')
def step_impl(context):
     
        
        context.driver = webdriver.Chrome("C:\ChromeDrivers\chromedriver.exe")
        context.driver.delete_all_cookies()
        context.driver.maximize_window()      



@given(u'magento website is opened')
def step_impl(context):
    context.driver.get("http://magento2demo.firebearstudio.com/")
    
@when(u'I click on sign in')
def step_impl(context):
        context.driver.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[2]").click()

@when(u'I enter email as "{email}"')
def step_impl(context,email):
    try:
        context.driver.find_element(By.XPATH,"//*[@id=\"email\"]").send_keys(email)
        assert True
    except:
        assert False

@when(u'I enter password as "{Pass}"')
def step_impl(context,Pass):
    try:
        context.driver.find_element(By.XPATH,"//*[@id=\"pass\"]").send_keys(Pass)
        assert True
    except:
        assert False

@when(u'I click sign in button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//*[@id=\"send2\"]").click()


@when(u'I click on cart')
def step_impl(context):
    time.sleep(15);
    context.driver.find_element(By.XPATH,"/html/body/div[2]/header/div[2]/div[1]/a").click()
    time.sleep(3);


@when(u'I click on remove button of product named as "{productName}"')
def step_impl(context,productName):  
    
    
    
    if("Voyage Yoga Bag"==productName):
        try:       

            context.driver.find_element(By.CSS_SELECTOR,".minicart-items .product-item:nth-child(1) .delete").click() 
            time.sleep(8)   
        except:
            assert False
    if("Rival Field Messenger"==productName):
        try:       
            context.driver.find_element(By.CSS_SELECTOR,".minicart-items .product-item:nth-child(2) .delete").click()
            time.sleep(8)
        except:
            assert False

    
    

@when(u'I click on ok')
def step_impl(context):
    time.sleep(4)
    context.driver.find_element(By.CSS_SELECTOR,"body > div.modals-wrapper > aside.modal-popup.confirm._show > div.modal-inner-wrap > footer > button.action-primary.action-accept").click()
    time.sleep(8)


@then(u'product named as "{product}" should not be in the cart')
def step_impl(context,product): 
        try:       
            time.sleep(10)
            time.sleep(5)
            soup = context.driver.find_elements(By.CSS_SELECTOR,"div.product .product-item-details .product-item-name")
            for el in soup:
                if(product in el.text):  
                    assert False
            assert True
                            
        except:
            assert False

    # .minicart-items .product-item:nth-child
    # .minicart-items .product-item:nth-child(1)  .product-item-name