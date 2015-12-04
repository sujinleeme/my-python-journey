import requests
def get_googlemap_url(place):
    baseurl = 'http://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'address' : place}
    data = requests.get(baseurl, params=params).json()
    channel = data['results'][0]
    address = channel['formatted_address']
    lat, lng = channel['geometry']['viewport']['northeast']['lat'], \
               channel['geometry']['viewport']['northeast']['lng']
    mapurl = 'https://www.google.co.kr/maps/place/'
    findurl = '{}{}/@{},{}'.format(mapurl, address, lat, lng)
    return ('{}\n{}'.format(address, findurl))

print (get_googlemap_url(str(input())))
