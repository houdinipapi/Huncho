import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('track_db.sqlite')
cur = conn.cursor()

# Creating new tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE 
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


file_name = input('Enter file name: ')
if len(file_name) < 1:
    file_name = 'Library.xml'


# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

def look_up(dictionary, key):
    found = False
    for child in dictionary:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


stuff = ET.parse(file_name)
all_stuff = stuff.findall('dict/dict/dict')
print('Dict count:', len(all_stuff))

for entry in all_stuff:
    if look_up(entry, 'Track ID') is None:
        continue
    name = look_up(entry, 'Name')
    artist = look_up(entry, 'Artist')
    album = look_up(entry, 'Album')
    count = look_up(entry, 'Play Count')
    rating = look_up(entry, 'Rating')
    length = look_up(entry, 'Total Time')

    if name is None or artist is None or album is None:
        continue

    print(name, artist, album, count, rating, length)
