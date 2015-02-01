"""
Takes data from twitter (in data.txt) and makes post request to Watson-IBM API to analyze the text for User modeling.
To run the file you need to have your own keys file in the directory above
"""

# ordering imports
# Standard Library modules
import json
# External/third party packages/modules
import requests
# Internal/self-written modules
from .. import keys

url = "https://gateway.watsonplatform.net/systemu/service/api/v2/profile"

username = keys.username
password = keys.password

with open ("data.txt", "r") as myfile:
    text=myfile.read().replace('\n', '')

raw_data = {
	'contentItems' : [{
	'userid' : username,
	'id' : 'dummyUuid',
	'sourceid' : 'freetext',
	'contenttype' : 'text/plain',
	'language' : 'en',
	'content': text 
	}]
}

input_data = json.dumps(raw_data)


response = requests.post(url, auth=(username, password), headers = {'content-type': 'application/json'}, data=input_data)
# print response.status_code # needed for testing
print response.text