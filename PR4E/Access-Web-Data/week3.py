#Description
'''
Course: Using Python to Access Web Data
Topic: BeautifulSoup
Date: 2015.11.12.
About: Networked Programs - socket, urllib
'''

#1. socket
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
while True:
    data = mysock.recv(512)
    if len(data)==0:
        break
    print(data.decode('utf-8'))
mysock.close()

#2. urllib
import urllib.request file = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in file:
  print(line.decode('utf-8').strip())
