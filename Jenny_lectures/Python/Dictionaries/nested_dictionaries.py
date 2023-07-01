student_data = {
    "Papi": {"reg_no": 3567, "age": 32, "Language": "Python"},
    "Houdini": {"reg_no": 4534, "age": 23, "Language": "JavaScript"},
}

print(student_data)
print(student_data["Papi"])
print(student_data["Papi"]["Language"])

# Adding a key to a nested dictionary
student_data["Papi"]["phone_no"] = 98767
print(student_data["Papi"])

# deleting
del student_data["Papi"]["phone_no"]  # Deleting phone number
print(student_data["Papi"])

# Returning a deleted item using the pop() function
print(student_data["Papi"].pop("Language"))