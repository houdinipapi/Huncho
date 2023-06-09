"""
- Implement a class called Jar with these methods:
    - __init__ should initialize a cookie jar with the given capacity,
    which represents the maximum number of cookies that can fit in the
    cookie jar.
    If capacity is not a non-negative int, though, __init__
    should instead raise a ValueError.
    - __str__ should return a str with 🍪, where n is the number of cookies
    in the cookie jar.
    For instance, if there are 3 cookies in the cookie jar,
    then str should return "🍪🍪🍪"
    - deposit should add n cookies to the cookie jar.
    If adding that many would exceed the cookie jar’s capacity, though,
    deposit should instead raise a ValueError.
    - withdraw should remove n cookies from the cookie jar. Nom nom nom.
    If there aren’t that many cookies in the cookie jar, though,
    withdraw should instead raise a ValueError.
    - capacity should return the cookie jar’s capacity.
    - size should return the number of cookies actually in the cookie jar.
"""


class Jar:
    # Initializing capacity
    def __init__(self, capacity=12):
        # Checking if the capacity is an integer & not a negative number
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError

        # Assigning the validated capacity.
        # '_capacity' indicates a private variable accessible within the class.
        self._capacity = capacity

        # Initializing an empty list as an instance variable.
        # --> Will be used to store cookies in the jar
        self.cookies = list()

    def __str__(self) -> str:
        # Returning a string
        return "🍪" * len(self.cookies)

    # Adding cookies to the jar
    def deposit(self, n):
        # Checking for excess addition of cookies
        if len(self.cookies) + n > self.capacity:
            raise ValueError("Execess Capacity")

        # Adding 'n' cookies to the list.
        # --> Each cookie is represented by the value 'None'
        self.cookies.extend([None] * n)

    # Removing a cookie from the jar
    def withdraw(self, n):
        # Checking if the jar has less cookies than the amount to be withdrawn
        if len(self.cookies) < n:
            raise ValueError("Insufficient Cookies")

        # Deleting the last 'n' elements from the list.
        # --> Slice notation
        del self.cookies[-n:]

    # Setter --> Providing a read-only access to the '_capacity' attribute
    @property
    def capacity(self):
        return self._capacity

    @property  # --> Allows to retrieve the number of cookies in the jar
    def size(self):
        return len(self.cookies)
