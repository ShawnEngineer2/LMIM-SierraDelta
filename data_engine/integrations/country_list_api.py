#This module integrates SierraDelta with the Country List API from RapidAPI (https://rapidapi.com/pkmi1550--HrZzGyyzHn/api/country-list5/)
from urllib import response
import requests as req
import json

class CountryListAPI(object):

    def __init__(self):
        pass

    def GetStatesForCountryID(self, country_code: int):
        #Retrieve the list of states for the country matching the Country API id code
        api_endpoint = "https://country-list5.p.rapidapi.com/statelist/"

        req_body = {"countryid": country_code}

        req_headers = {
            "content-type": "application/json",
	        "X-RapidAPI-Key": "b8daf5cb99msh3796e1ca4339b57p16d281jsn91338f66203b",
	        "X-RapidAPI-Host": "country-list5.p.rapidapi.com"
        }

        resp_data: req.Response = req.request("POST", api_endpoint, json=req_body, headers=req_headers)

        print(resp_data.status_code, resp_data.text)

