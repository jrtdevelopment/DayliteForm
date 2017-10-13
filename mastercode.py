import pprint #Imports for pretty print
import requests #Imports for http requests to handle the API
import json #Imports the JSON handler

apiKey = 'Bearer h0r05NIGxn2K1I46Gfb5xsC3DeqZRL' #Put the API key here, saves you having to copy and past it into your code

r = requests.get('https://api.marketcircle.net/v1', headers={'Authorization': apiKey}, verify=False) #Gives the r variable the value of requests get

print r.status_code #Print the value of the status code of r
print r.headers['content-type'] #print the value of the headers of the request
  
print "GetUserDetails"
print "This script will take the First name and surname from a form and list all users with those details"

print "This line shows what values have been passed from the form to the service."
firstName = Hook['params']['firstname']
lastName = Hook['params']['lastname']
email = Hook['params']['email']
print firstName
print lastName
print email
# This line gets all the contacts.
r = requests.get('https://api.marketcircle.net/v1/contacts', headers={'Authorization': apiKey}, verify=False)
print r.encoding
print r.content
