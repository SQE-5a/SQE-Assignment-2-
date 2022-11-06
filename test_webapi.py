import requests 
import json
import jsonpath
import pytest

urlIs="http://magento2demo.firebearstudio.com/rest/all/V1/directory/currency/"

def test_directoryCurrencyInformationAcquirerV1():
    response=requests.get(urlIs)
    json_response = json.loads(response.text)
    print(response.content)
    currency = jsonpath.jsonpath(json_response,'base_currency_code')
    assert currency[0]=='USD'
    currency_symbol = jsonpath.jsonpath(json_response,'base_currency_symbol')
    assert  currency_symbol[0]=='$'
    currency = jsonpath.jsonpath(json_response,'default_display_currency_code')
    assert currency[0]=='USD'
    currency_symbol = jsonpath.jsonpath(json_response,'default_display_currency_symbol')
    assert currency_symbol[0]=='$'
