# <-- LEARNING ABOUT NETWORKED PROGRAMS --> #

import socket
import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup

# Creating an HTTP Request in Python
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
my_sock.send(cmd)

while True:
    data = my_sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

my_sock.close()

# -- ASCII -- #
# char = input('Enter a single character: ')
# print(ord(char))  # ==> Returns the ASCII value of the character


# Using urllib in Python
f_hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')  # --> requesting Python to open url

for line in f_hand:
    print(line.decode().strip())  # --> Printing the contents of the url 'WITHOUT THE HEADERS'

# Treating the url like a file
f_hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()

for line in f_hand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)


# Reading Web-pages

f_hand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

for line in f_hand:
    print(line.decode().strip())  # --> reading through webpages


# -- Scraping Web Pages -- #
url = input('Enter a link: ')

# Ignoring SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
