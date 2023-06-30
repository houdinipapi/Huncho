# Simple greeting function
def greet():
    print("Hello")
    print("World")

greet()

# With an argument
name = input("Name: ")

def new_greet(name):
    print(f"Hi, {name}")

new_greet(name)

# Sum function
def add_num(a, b):
    return a + b

print(add_num(5, 7))