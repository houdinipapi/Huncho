# <-- LEARNING ABOUT NETWORKED PROGRAMS --> #

import socket
import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import json

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
url = 'https://twitter.com/home'

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


# --> XML <-- #

# This is an XML code  --> Python will be reading through this code
data = '''
<person>
    <name>Houdini</name>
    <phone type="international">
        +245 197 450 116
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)  # Python extracting the name from the XML code
print('Attribute:', tree.find('email').get('hide'))  # Extracting the attribute

XML_input = '''
<stuff>
    <users>
        <user x='2'>
            <id>001</id>
            <name>Cliff</name>
        </user>
        <user x='7'>
            <id>009</id>
            <name>Papi</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(XML_input)  # --> Getting the info in string format from XML
lst = stuff.findall('users/user')  # --> Finding all user in users and storing it in a list ==> '/users/user' is a path
print('User count:', len(lst))  # --> Printing the length of the list

for item in lst:  # --> Looping through the created list
    print('Name:', item.find('name').text)  # --> Finding the name element and printing the text held within it.
    print('ID:', item.find('id').text)  # --> Finding the id element and printing the text within it.
    print('Attribute:', item.get('x'))  # --> Getting the attribute that is within an element.

# --> JSON (JavaScript Object Notation) <-- #

# The code below is in JSON format --> Always use double quotes
# data in this case is an object NOT a dictionary
data = ''' {
    "name": "My Name",
    "phone": {
        "type": "international",
        "number": "+752 453 234 893"
    },
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data)  # --> This is decoding the data presented in JSON format.
print('Name:', info["name"])  # --> Printing the property ==> Resembles a dictionary whereby we have key value pairs.
print('Hide:', info["email"]["hide"])  # --> Accessing the hide property which is within the email property.


# N/B:--> JSON represents data as nested "lists" and "dictionaries"

# Decoding an JSON object in a list
JSON_input = '''[
    { "id": "001",
      "x": "2",
      "name": "My Name"
    },
    { "id": "009",
      "x": "7",
      "name": "Second Name"
    }
]'''

new_info = json.loads(JSON_input)  # --> Parsing a JSON string into a Python object.
print('User Count:', len(new_info))  # --> Calculating the length of the list
print(new_info)
for item in new_info:
    print('Name:', item['name'])
    print('ID:', item['id'])
    print('Attribute:', item['x'])


# Reading data from Google Maps API
api_key = False

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else:
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter your address: ')
    if len(address) < 1:
        break

    parameters = dict()
    parameters['address'] = address
    if api_key is not False:
        parameters['key'] = api_key

    url = service_url + urllib.parse.urlencode(parameters)

    print('Retrieving', url)
    new_url_open = urllib.request.urlopen(url)
    data = new_url_open.read().decode()
    print('Retrieved:', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failed To Retrieve ===')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    latitude = js["results"][0]["geometry"]["location"]["lat"]
    longitude = js["results"][0]["geometry"]["location"]["lng"]
    print('Latitude:', latitude, 'Longitude:', longitude)
    location = js['results'][0]['formatted_address']
    print('Location:', location)
