import urllib.request, urllib.parse, json, ssl
scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

#request and open URL
city = input()
baseurl = "https://query.yahooapis.com/v1/public/yql?q="
yql_query = 'select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text="%s")'% city
yql_url = baseurl + urllib.parse.quote(yql_query, encoding='utf-8')+ "&format=json&env=store://datatables.org/alltableswithkeys"
result = urllib.request.urlopen(yql_url, context=scontext).read()
data = json.loads(result.decode('utf-8'))
data = json.dumps(data)
print (data.strip('condition'))
