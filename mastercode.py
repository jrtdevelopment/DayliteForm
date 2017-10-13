import pprint #Imports for pretty print
import requests #Imports for http requests to handle the API
import json #Imports the JSON handler

apiKey = 'Bearer h0r05NIGxn2K1I46Gfb5xsC3DeqZRL' #Put the API key here, saves you having to copy and past it into your code

r = requests.get('https://api.marketcircle.net/v1', headers={'Authorization': apiKey}, verify=False) #Gives the r variable the value of requests get

print r.status_code #Print the value of the status code of r
print r.headers['content-type'] #print the value of the headers of the request
  
print "Welcome to MasterCode"
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
payload = {'first_name':firstName, 'last_name':lastName}

payload = json.dumps(payload)
r = requests.post('https://api.marketcircle.net/v1/contacts', headers={'Authorization': apiKey}, data=payload, verify=False)
print r.status_code