import csv
import json
import requests

jwtToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJOVVJyNjBBTFNwMlV6Q1hFWjRVNUlnIiwiZXhwIjoxNTg1OTU2MjQwfQ.HDtlzpSiDY6TWMoM3Qtzkj09oCVNarpasqQPM0_Dwo4"

def checkUser(email):	
	existingEmails = []
	listUserHeaders = {
	    'Accept': 'application/json, application/xml',
	    'Authorization': 'Bearer ' + jwtToken,
	    'Content-Type': 'application/json'
	}

	params = {
		'page_size': '300'
	}

	response = requests.get('https://api.zoom.us/v2/users/', headers=listUserHeaders, params=params)
	users = json.loads(response.content)['users']

	for user in users:
	    existingEmails.append(str(user['email']))


	if email in existingEmails:
		return True
	else: return False


