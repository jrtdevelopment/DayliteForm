import pprint #Imports for pretty print
import requests #Imports for http requests to handle the API
import json #Imports the JSON handler

apiKey = 'Bearer nR377HuRfL8WM33yQZsJ76t7RpUKkj' #Put the API key here, saves you having to copy and past it into your code

r = requests.get('https://api.marketcircle.net/v1', headers={'Authorization': apiKey}, verify=False) #Gives the r variable the value of requests get

print r.status_code #Print the value of the status code of r
print r.headers['content-type'] #print the value of the headers of the request
  
print "Welcome to the Daylite API test service"
print "Hook['params'] is populated with the following request parameters"
pprint.pprint(Hook['params'])
firstName = Hook['params']['firstname']
lastName = Hook['params']['lastname']
email = Hook['params']['email']
print firstName
print lastName
print email
#r = requests.get('https://api.marketcircle.net/v1/contacts', headers={'Authorization': apiKey}, verify=False)
#print r.encoding
#print r.content
payload = {'first_name':firstName}

payload = json.dumps(payload)

pprint payload
#r = requests.post('https://api.marketcircle.net/v1/contacts', headers={'Authorization': apiKey}, json=payload)
#print r.status_code
