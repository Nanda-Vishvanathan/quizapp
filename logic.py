import requests
import json,random

def get_country_details():
    """1. This method is to extract the countries fromt the api specified and is converted
     to python dictionary for accessing the values. 
    Note: API has been hardcoded. But when deploying to test/pre-prod/production- value 
    needs to be in a config file.
    2. This method also generates random numbers for the length of total countries extracted 
    from the api Also the list is shuffled.

    """
    response_details = requests.get('https://countriesnow.space/api/v0.1/countries/capital')
    response_data = response_details.content
    pd_data = json.loads(response_data)
    pd_value = pd_data["data"]
    list_number=[i for i in range(0,len(pd_value))]
    random.shuffle(list_number)
    return pd_value,list_number
