#Description
'''
Course: Using Python to Access Web Data
Topic: retrieve and parse XML (eXtensible Markup Language) data
Date: 2015.11.25.
About: xml.etree.ElementTree
'''

#Code
import urllib.request
import xml.etree.ElementTree as ET

xml = ET.fromstring(urllib.request.urlopen('http://python-data.dr-chuck.net/comments_42.xml').read())
count = [int(data.text) for data in xml.getiterator('count')]
print ('sum :',(sum(count)))
