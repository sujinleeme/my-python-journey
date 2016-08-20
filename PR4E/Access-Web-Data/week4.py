#Description
'''
Course: Using Python to Access Web Data
Topic: BeautifulSoup
Date: 2015.11.19

About: write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py.
The program will use urllib to read the HTML from the data files below,
extract the href= vaues from the anchor tags,
scan for a tag that is in a particular position relative to the first name in the list,
follow that link and repeat the process a number of times and report the last name you find.

Test Case:
- start at http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html
- Find the link at position 3 (the first name is 1). Follow that link.
- Repeat this process 4 times. The answer is the last name that you retrieve.
- Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
- Last name in sequence: Anayah
'''

import re
import urllib.request
from bs4 import BeautifulSoup

#input
url = str(input('Enter url: '))
position = (int(input('Enter position: '))-1)
process = int(input('Enter process: '))

data = []
while process > 0:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]
    url = (links[position])
    data.append(url)
    process -= 1

#last output
lastUrl = data[-1]
print ((re.search(r'(?<=known_by_)[\w\.]+(?=.html)', lastUrl).group()))
