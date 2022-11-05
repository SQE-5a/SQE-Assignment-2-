import requests 
import json
import jsonpath

url="http://magento2demo.firebearstudio.com/rest/all/V1/applepay/auth"
def test_payPalBraintreeAuthV1():
    response=requests.get(url)
    json_response = json.loads(response.text)
    pages = jsonpath.jsonpath(json_response,'client_token')
    assert pages[0]==''
    pages_symbol = jsonpath.jsonpath(json_response,'display_name')
    assert pages_symbol[0]=='Store'
    pages_symbol = jsonpath.jsonpath(json_response,'action_success')
    assert pages_symbol[0]=='http://magento2demo.firebearstudio.com/checkout/onepage/success/'
    pages_symbol = jsonpath.jsonpath(json_response,'logged_in')
    assert pages_symbol[0]==0
    # 0 means false
    pages_symbol = jsonpath.jsonpath(json_response,'store_code')
    assert pages_symbol[0]=='admin'