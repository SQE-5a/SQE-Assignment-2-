import requests 
import json
import jsonpath
import pytest

urlIs="http://magento2demo.firebearstudio.com/rest/all/V1/directory/countries/AD"
# last string is parameter:like here below AD is parameter:countryId 
def test_directoryCountryInformationAcquirerV1():
    response=requests.get(urlIs)
    json_response = json.loads(response.text)
    pages = jsonpath.jsonpath(json_response,'id')
    assert pages[0]=='AD'
    pages_symbol = jsonpath.jsonpath(json_response,'two_letter_abbreviation')
    assert pages_symbol[0]=='AD'
    pages_symbol = jsonpath.jsonpath(json_response,'three_letter_abbreviation')
    assert pages_symbol[0]=='AND'
    pages_symbol = jsonpath.jsonpath(json_response,'full_name_locale')
    assert pages_symbol[0]=='Andorra'
    pages_symbol = jsonpath.jsonpath(json_response,'full_name_english')
    assert pages_symbol[0]=='Andorra'