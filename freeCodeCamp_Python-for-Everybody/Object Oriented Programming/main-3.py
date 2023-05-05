# --- OBJECT ORIENTED PROGRAMING --- #

# Sample of a code that is object-oriented
class PartyAnimal:  # --> This is the template for making PartyAnimal objects
    x = 0  # --> Each PartyAnimal object has a bit of data

    def party(self):
        self.x = self.x + 1
        print("So far:", self.x)


an = PartyAnimal()  # --> Constructing a PartyAnimal object and store in 'an'
an.party()  # --> Telling the 'an' object to run the party() code within it
an.party()
an.party()
an.party()


# Playing with dir() and type()
y = 'Hello There'
print(type(y))  # --> This will tell you that y is a 'string' data type
print(dir(y))  # --> This expounds the methods and functions that y accepts and also Python construction parameters

# --> dir() looks for capabilities

print(dir(an))


# -- Object Lifecycle -- #
# - Objects are created, used, and may sometimes be destroyed
# Constructors are used more often compared to destructors.
# The primary purpose of the constructor is to set up some instance variables...
# to have the proper initial values when the object is created.

class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed', self.x)  # The object is constructed when x = 0

    def party(self):  # Whenever party() is called, the cont should increase by 1
        self.x += 1
        print('So far:', self.x)

    def __del__(self):
        print('I am destructed', self.x)  # The destruction happens after the last increment of the value


an = PartyAnimal()
an.party()
an.party()

# 'an' is destroyed and assigned a new value  --> 'I am destructed at 2'

an = 42  # 'New value is assigned to an' Just before this, the destruction happens to create room for the new value.
print('Now "an" contains', an)


# --> INHERITANCE <-- #
# Mantra:- Write one and use it many times
# - The new class(child) has all the capabilities of the old class(parent) and then some more.
# - The subclasses are more specialized versions of a class,
#   which inherit attributes and behaviors from their parent classes,
#   and can introduce their own.

class PartyAnimal:  # --> Parent
    x = 0

    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")

    def party(self):
        self.x += 1
        print(self.name, "party count", self.x)


class FootballFan(PartyAnimal):  # --> Child inherits the properties of the Parent
    points = 0

    def touchdown(self):
        self.points += 7
        self.party()

        print(self.name, "points", self.points)


new = FootballFan("Papi")
new.touchdown()
new.touchdown()
new.touchdown()

new = PartyAnimal("Houdini")
new.party()
new.party()
new.party()

# --- DEFINITIONS -- #
# Class - A template.
# Attribute - A variable within a class.
# Method - A function within a class.
# Object - A particular instance of a class.
# Constructor - Code that runs when an object is created.
# Inheritance - The ability to extend a class to make a new class
# --- END --- #
