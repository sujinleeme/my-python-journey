# About file
'''
Course: Using Python to Access Web Data
Topic: BeautifulSoup
Date: 2015.11.19
About: write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py.
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
scan for a tag that is in a particular position relative to the first name in the list,
follow that link and repeat the process a number of times and report the last name you find.
'''

import urllib.request
from bs4 import BeautifulSoup

#input
position = int(input('position: '))-1
process = int(input('process: '))
url = str(input('url: '))

data = []
while process > 0:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]
    url = (links[position])
    data.append(url)
    process -= 1

#last output
print (data[-1])
