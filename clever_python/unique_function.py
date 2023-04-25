"""
Create a function unique that takes
in a list and returns only unique items
#>>>(['ruby', 'ruby', 'pyhon'])
['ruby', 'python']
"""


def unique_func():
    list1 = ['ruby', 'ruby', 'python']
    return list(set(list1))


print(unique_func())


#unique = lambda languages = ['ruby', 'ruby', 'python']: list(set(languages))

#print(unique())
