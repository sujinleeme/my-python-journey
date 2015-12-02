#1. Json 
''' sum list of count '''

import urllib.request
import requests
url = 'http://python-data.dr-chuck.net/comments_190126.json'
data = requests.get(url).json()
x = sum([i['count'] for i in (data['comments'])])
print (x)

#2. Calling JSON API
''' retrieve the first place_id from the JSON.
A place ID is a textual identifier that uniquely identifies a place as within Google Maps.'''
import requests
def get_placeID(place):
    baseurl = 'http://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'address' : place}
    data = requests.get(baseurl, params=params).json()
    return (data['results'][0]['place_id'])

print (get_placeID(str(input())))
