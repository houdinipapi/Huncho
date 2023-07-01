student_data = [
    {"Name": "Papi", "Age": 34, "Reg_no": 4632, "Language": "Python"},
    {"Name": "Houdini", "Age": 45, "Reg_no": 2321, "Language": "JavaScript"},
]


# function that adds student data
def add_new_student(name, age, reg_no, language):
    new_student = dict()
    new_student["Name"] = name
    new_student["Age"] = age
    new_student["Reg_no"] = reg_no
    new_student["Language"] = language

    # Adding to the list
    student_data.append(new_student)


add_new_student("Chulo", 25, 3674, "Java")
print(student_data)
