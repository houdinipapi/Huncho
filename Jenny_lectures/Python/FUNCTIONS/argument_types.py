# Types of arguments
# Default
# Positional
# Keyword
# Arbitrary :-
#     - Arbitrary positional
#     - Arbitrary keyword

# Positional
def greet(name, dept):
    print(f"Hello, {name}.\nWelcome to {dept} department.")

greet("Papi", "Fashion & Design")

# Keyword Arguments
greet(name="Houdini", dept="Engineering")

# Positional & Keyword
greet("Chulo", dept="Medicine")  # Keyword argument should be after positional argument to avoid syntax error.

# Default Argument
def new_greeting(name, dept, subject="Python"):
    print(f"Hello {name}.\nThis is {dept} department.\nWe teach {subject}.")

new_greeting("Houdini", "Applied Science")  # Will take default subject.
new_greeting("Cliff", "Software", "JavaScript")  # Javascript will overwrite the default subject.

# Arbitrary Arguments  --> Can take any amount of variables
def addition(*numbers):
    total_sum = 0
    for i in numbers:
        total_sum += i
    print(f"Sum: {total_sum}")

addition(5, 6, 7, 8)
addition(2, 3, 4, 5, 6, 7, 8, 9)
