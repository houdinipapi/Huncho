# <-- LEARNING ABOUT NETWORKED PROGRAMS --> #

import socket
import urllib.request, urllib.parse, urllib.error

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
