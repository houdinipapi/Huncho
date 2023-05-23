# These import statements allow the program to use functions and classes defined in the 'json' and 'sqlite3' modules.
import json
import sqlite3

# Creating a connection to a SQLite database named 'roster_db_sqlite'.
# Creating a cursor object that will be used to execute SQL commands in the database.
conn = sqlite3.connect('roster_db.sqlite')
cur = conn.cursor()

# -- SETTING UP THE DATA -- #

# Executing an SQL script that drops any existing 'User', 'Member', and 'Course' tables in the database.
# Creates new tables with the specified schema.
cur.executescript("""
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Course (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title   TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);
""")

# Prompting the user to enter a filename for a JSON data file.
# If no filename is entered, the default filename 'roster_data_sample.json' will be used.
file_name = input('Enter file name: ')
if len(file_name) < 1:
    file_name = 'roster_data_sample.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

# Reading the contents of the JSON data file into a string.
# Parsing the string into a Python object using the 'json.loads()' function.
string_data = open(file_name).read()
json_data = json.loads(string_data)

# Looping through the list of JSON data entries and extracting the 'name' and 'title' fields.
# For each entry, the script checks if a corresponding 'User' and 'Course' record exists in the database,
# and creates new records if necessary.
# The loop then creates a new 'Member' record linking the 'User' and 'Course' records.
# Finally, the script commits the changes to the database.
for entry in json_data:
    name = entry[0]
    title = entry[1]

    print((name, title))

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES (?)''', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES (?)''', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id) VALUES (?, ?)''',
                (user_id, course_id))

    conn.commit()
