#1. Json
import urllib.request
import requests
url = 'http://python-data.dr-chuck.net/comments_190126.json'
data = requests.get(url).json()
x = sum([i['count'] for i in (data['comments'])])
print (x)

2. Calling JSON API
