#1. Json 
''' sum list of count '''
import urllib.request
def count(url):
    data = requests.get(url).json()
    return sum([i['count'] for i in (data['comments'])])
    
print (cout('http://python-data.dr-chuck.net/comments_190126.json')

#2. Calling JSON API
'''
retrieve the first place_id from the JSON.
A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
'''
import requests
def get_placeID(place):
    baseurl = 'http://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'address' : place}
    data = requests.get(baseurl, params=params).json()
    return (data['results'][0]['place_id'])

print (get_placeID(str(input())))
