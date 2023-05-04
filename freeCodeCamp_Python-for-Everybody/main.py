# --IMPORTED MODULES
import re
import socket

# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# FINDING LARGEST NUMBER

num_list = [6, 7, 8, 23, 47, 45, 12]

great_num = num_list[0]
for num in num_list:
    if num > great_num:
        great_num = num

print(f"The largest number is: {great_num}")

# COUNTING ITEMS IN A LIST
count = 0
for num in num_list:
    count += 1
    print(count, num)

print(f"The number of items is: {count}")


# ADDING THE TOTAL SUM OF ITEMS IN A LIST
total_sum = 0
for num in num_list:
    total_sum += num

print("The total sum is:", total_sum)


# AVERAGE OF NUMBERS IN A LIST
average = total_sum / count

print(average)


# FILTERING NUMBERS IN A LIST
print("Numbers greater than or equal to 20 in the list:")
for num in num_list:
    if num >= 20:
        print(num)

# SEARCHING USING A BOOLEAN VALUE
found = False
for num in num_list:
    if num == 23:
        found = True

print("The value is", found)


# FINDING THE SMALLEST NUMBER IN A LIST
small_num = num_list[0]
for num in num_list:
    if num < small_num:
        small_num = num

print(f"The Smallest number is: {small_num}")

# FINDING LENGTH OF A STRING
name = "Houdini"
count = 0
for i in name:
    count += 1

print(f"The length of the string is: {count}")

# LOOPING THROUGH STRINGS
fruit = 'banana'
index = 0

while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1


# USING A FOR LOOP
# index = 0
# for i in fruit:
#     index += 1
#     print(index, i)

# COUNTING THE APPEARANCE TIMES OF A CHARACTER:
word = 'banana'
count = 0
for i in word:
    if i == 'a':
        count += 1

print(f"The character 'a' appears {count} times.")

# SLICING A STRING
word_str = "Monty Python"
print(word_str[:5])
print(word_str[2:5])
print(word_str[:])
print(word_str[3:])


# STRING CONCATENATION
greet = 'Hello'
name = 'Papi'
print(greet + ' ' + name)


# USING in AS A LOGICAL OPERATOR
name = 'Papi'
if 'a' in name:
    print('Found it')
else:
    print('Not Found')


# STRING COMPARISON
# name = input("Enter your name: ")
# if name == 'papi':
#     print('same as papi')
# elif name > 'papi':
#     print('Greater than papi')
# else:
#     print('Lower than papi')


# STRING LOWERCASE/UPPERCASE
name = 'python'
print(name.upper())
print(name.lower())


# SEARCHING A STRING --> Prints the position
name = 'Monty Python'
print(name.find('ho'))
print(name.find('xx'))  # --> Returns -1 if the characters are not in the string


# SEARCH AND REPLACE
name = 'Hello World'
print(name.replace('o', 'x'))  # --> finds 'o' and replaces it with 'x'


# STRIPPING/REMOVING WHITESPACE
name = ' Papi Houdini'
print(name.lstrip())    # --> Removes the whitespace on the left
new_name = 'Papi Houdini '
print(new_name.rstrip())  # --> Removes the whitespace on the right
name_str = ' Papi Houdini '
print(name_str.strip())  # --> Removes whitespace on either side or basically both sides


# PREFIXES
name = 'Papi'
if name.startswith('P'):
    print('Name starts with P')
else:
    print('Name does not start with P')


# PARSING & EXTRACTING
data = 'My name is Papi Houdini and my email is houdini@github.com, what about you?'

# Extracting 'houdini@github.com'
h_position = data.find('h')  # --> Finds the first letter of the email
print(h_position)

comma_position = data.find(',', h_position)  # --> Finds the character that comes after the last letter in the email
print(comma_position)

user_email = data[h_position:comma_position]  # --> Slicing beginning at the first letter up-to the last in the email
print(user_email)


# READING FILES

# handle = ope(filename, mode)
# r --> read
# w --> write
f_hand = open('../../first.py', 'r')
print(f_hand)

# Printing each line in a file
for line in f_hand:
    print(line)

# Counting the number of lines in a file:
f_hand = open('../../second.py')
count = 0

for line in f_hand:
    count += 1
print(count)

# Slicing a file
f_hand = open('../../first.py')  # --> Opening a file
inp = f_hand.read()  # --> Reading through the characters inside a file
print(len(inp))  # --> Printing the length of all the characters inside that file
print(inp[:25])  # --> Slicing the file contents from the beginning up-to but not including 20th position

# Searching through a file
f_hand = open('../../safe_box.py')
for line in f_hand:  # --> Iterating through the file contents
    if line.startswith('print'):  # --> Searching for a specific string
        print(line)

# Searching through a file(fixed -- omitting automatic newlines)
f_hand = open('../../safe_box.py')
for line in f_hand:
    line = line.rstrip()  # --> This omits the automatic new lines
    if line.startswith('print'):
        print(line)

# Skipping with continue:
f_hand = open('../../safe_box.py')
for line in f_hand:
    line = line.rstrip()
    if not line.startswith('row'):  # --> If the line does not start with 'row' continue searching
        continue
    print(line)

# Handling bad file names:
# f_name = input('Enter a file name: ')
# try:
#     f_hand = open(f_name)
# except:
#     print(f'{f_name} does not exist.')
#     quit()
# count = 0
# for line in f_hand:
#     if line.startswith('print'):
#         count += 1
# print(f'There are {count} lines in {f_name} starting with "print".')


# LISTS
fruit_list = ['mango', 'pear', 'banana']
print(fruit_list)

# Indexing and Lookup --> Printing each item with its index
for index, fruit in enumerate(fruit_list):
    print(index, fruit)

# Finding the length of the list
print(f'The length is: {len(fruit_list)}')

# Modifying the list
fruit_list[0] = 'apple'
print(fruit_list)

# Adding an item at the end
fruit_list.append('oranges')
print(fruit_list)

# Sorting the list --> Sorts the items/fruits alphabetically
fruit_list.sort()
print(fruit_list)

# Finding Max and Min
print(max(fruit_list))
print(min(fruit_list))

# Converting a string into a list
sample_str = "My email is houdini@github.com"
new_list = sample_str.split()
print("List:", new_list)

# Parsing the list --> Splitting the list further
print(new_list[3])
par_list = new_list[3].split('@')
print(par_list)

# Slicing lists
sample_list = ['mike', 'david', 'robert', 'patrick']
print(sample_list[1:2])
print(sample_list[-1])  # --> Prints the last element
print(list(reversed(sample_list)))  # --> Reverses the list

# Removing an item from the list
sample_list.remove('david')
print(sample_list)

# removing the last item in a list
sample_list.pop()
print(sample_list)


# --DICTIONARIES-- #

# Initializing an empty dictionary
new_dict = dict()

# adding elements into the dictionary
new_dict['age'] = 21
new_dict['name'] = 'Papi'
new_dict['Location'] = 'Nairobi'
print(new_dict)

# COUNTING
nums = [2, 5, 6, 3, 2, 6, 7, 2, 1, 7, 8, 9, 5]
db = dict()

# Looping through the list and checking the appearance times
for number in nums:
    db[number] = db.get(number, 0) + 1

print(db)


# COUNTING WORDS --> COUNTING PATTERN

# # Taking user's input
# phrase = input("Enter a paragraph of words:\n")
# # Splitting it into a list
# words = phrase.split()
# print(words)
# # Initializing an empty dictionary
# count_dict = dict()
# # Iterating through the list while keeping count of the items
# for word in words:
#     count_dict[word] = count_dict.get(word, 0) + 1
#
# print("Total words:", count_dict)

# COUNTING WORDS IN A FILE
f_name = input('Enter the file name: ')
f_handle = open(f_name)

new_dict = dict()
for line in f_handle:
    words_list = line.split()

    # print(words_list)

    for word in words_list:
        new_dict[word] = new_dict.get(word, 0) + 1

big_count = None
big_word = None
for word, count in new_dict.items():
    if big_count is None or count > big_count:
        big_count = count
        big_word = word

print(big_word, big_count)


# --TUPLES -- #
intro = ('name', 'age')
print("This is a tuple:", intro)


# Tuples and Assignment
(name, age) = ('Houdini', 23)
print(name)  # --> Prints 'Houdini'
print(age)  # --> Prints 23

new_dict = dict()
new_dict['name'] = 'Houdini'
new_dict['age'] = 23
new_dict['laptop'] = 'Windows'

print(new_dict)  # --> Prints the dictionary
print(list(new_dict))  # --> Prints a list ['name', 'age', 'laptop']
print(list(new_dict.items()))  # --> Prints a list that has tuples inside it

# Comparison in Tuples
if (9, 2, 3) > (4, 5, 6):  # --> Only the first item in the tuple will be counter-checked on both sides.
    print(True)  # --> The comparison operator goes from left to right
else:
    print(False)


# SORTING TUPLES
sample_dict = {'name': 'Houdini', 'county': 'Nairobi', 'age': 'twenty-three', 'weight': 'seventy-five'}
print(sample_dict)  # --> Printing the dictionary
print(list(sample_dict))  # --> Only prints the keys as a list
print(list(sample_dict.items()))  # --> Prints a list containing key:value as tuples
print(sorted(sample_dict))  # --> It will sort but only give the keys in a list
print(sorted(sample_dict.items()))


# Key Value
new_list = sorted(sample_dict.items())
print(new_list)
for key, value in new_list:
    print(f"Key ---> {key}  Value ---> {value}")  # --> Prints the key and value


# Sorting by values instead of keys:
print("--SORTING BY VALUE--")
print(new_dict)
print(new_list)

value_key_list = list()
for key, value in new_list:
    value_key_list.append((value, key))
print("Reversed key and value:")
print(sorted(value_key_list))  # --> Automatically sorts in ascending order

value_key_list = sorted(value_key_list, reverse=True)  # --> Sorts in descending order
print("Reversed and Sorted")
print(value_key_list)


# Looking for top 10 most words:
f_name = input("Enter a file name: ")  # --> Asking for a file name
f_hand = open(f_name)  # --> Opening the file
counts = dict()  # --> Initializing an empty dictionary

for line in f_hand:  # --> Iterating the lines of a given file
    words = line.split()  # --> Splitting lines into a list of words
    for word in words:  # --> Iterating the list of words
        counts[word] = counts.get(word, 0) + 1  # --> Counting each times a word appears
print(counts)  # --> Printing the dictionary ==> (key: value) == (word: no. of times)

lst = list()  # --> Initializing an empty list
for key, value in counts.items():  # --> Iterating the tuples created from a dict to a list
    new_tup = (value, key)  # --> Creating a new tuple with reverse position i.e (value, key)
    lst.append(new_tup)  # --> Appending the new tuples to the empty list
print(lst)  # --> Printing the list

lst = sorted(lst, reverse=True)  # --> Sorting the list tuples in reverse N/B:- Only values are being compared
print(lst)  # --> Printing the list

for value, key in lst[:10]:  # --> Checking for the top 10 words i.e., from 0th up-to but not including 10th
    print(key, value)  # --> Printing the tuple i.e., key and value


# --ALTERNATIVE TO LOOKING FOR THE TOP TEN MOST WORDS-- #
print("ALTERNATIVE METHOD:-")
c = {'the': 50, 'one': 20, 'of': 78, 'a': 125}
print(sorted([(v, k) for k, v in c.items()]))  # --> Will print the list of tuples in ascending order


# --REGULAR EXPRESSIONS:  --> The module is imported at the top of the file.
f_name = input('Enter a file name: ')
f_hand = open(f_name)

for line in f_hand:
    line = line.rstrip()
    if re.search('print', line):  # --> Searches for lines that have 'print' inside them
        print(line)

f_name = input('Enter a file name: ')
f_hand = open(f_name)

for line in f_hand:
    line = line.rstrip()
    if re.search('^print', line):  # --> Specifically searches for lines that begin with print
        print('Starts with:', line)


# Matching and Extracting data using RegEx
x = 'My 2 favorite numbers are 7 and 9'
y = re.findall('[0-9]+', x)
print(y)  # --> prints ['2', '7', '9']
y = re.findall('[AEIOU]+', x)
print(y)  # --> Returns an empty list


# Greed matching (+ and *)
x = 'From: Using the: character'
y = re.findall('^F.+:', x)  # --> Returns ['From: Using the:']
print(y)


# Non-Greedy matching (+? and *?)
y = re.findall('^F.+?:', x)
print(y)  # --> prints ['From:']


# Fine-tuning String Extraction
x = 'From papihoudini@github.com Sat Jan 6 09:15:39 2008'
y = re.findall('\\S+@\\S+', x)  # --> Returns ['papihoudini@github.com'] --> Used \\ to ignore
print(y)

y = re.findall('^From (\\S+@\\S+)', x)
print(y)

# Even Cooler Regex version
y = re.findall('^From .*@([^ ]*)', x)
print(y)


# Spam Confidence  --> Finding the string with most occurrences in lines starting with 'print'
f_name = input("Enter file name: ")
f_hand = open(f_name)

num_list = list()
for line in f_hand:
    line = line.rstrip()
    stuff = re.findall('print ([a-z.]+)', line)  # --> RegEx to find a string in lines beginning with 'print'

    if len(stuff) != 1:
        continue
    num = stuff[0]
    num_list.append(num)
print('Maximum string:', max(num_list))  # --> Finding the maximum string

# HTTP REQUEST IN PYTHON

print("MAKING A HTTP REQUEST IN PYTHON:")
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
