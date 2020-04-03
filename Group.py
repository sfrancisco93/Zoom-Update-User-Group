import json
import requests
import io

jwtToken = ""

if __name__ == "__main__":
	main()

isascii = lambda s: len(s) == len(s.encode())
existingGroups = {}

def getGroups():
	listUserHeaders = {
	    'Accept': 'application/json, application/xml',
	    'Authorization': 'Bearer ' + jwtToken,
	    'Content-Type': 'application/json'
	}

	params = {
		'page_size': '300'
	}

	response = requests.get('https://api.zoom.us/v2/groups/', headers=listUserHeaders, params=params)
	groups = json.loads(response.content)['groups']
	for item in groups:
		existingGroups[item['name']] = item['id']


def checkGroup(item):	
	getGroups()

	if item in existingGroups:
		return True
	else: return False

def updateUserGroup(file):
	groupId = 'test'
	for item in file.keys():
		print(item)
		print existingGroups[item]

		listUserHeaders = {
		    'Accept': 'application/json, application/xml',
		    'Authorization': 'Bearer ' + jwtToken,
		    'Content-Type': 'application/json'
		}

		for item2 in file[item]:
			print(item2)
			body = {
				"members": [
				{
					"email":item2
				}]
			}
			print('https://api.zoom.us/v2/groups/' + existingGroups[item] + '/members')
			response = requests.post('https://api.zoom.us/v2/groups/' + existingGroups[item] + '/members', headers=listUserHeaders, json=body)
			groups = json.loads(response.content)
			print(groups)

def main():
	getGroups()
	updateUserGroup('na')