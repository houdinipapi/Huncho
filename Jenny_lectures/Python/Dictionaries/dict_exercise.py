student_marks = {
    "Papi": 98,
    "Houdini": 89,
    "Chulo": 96,
    "Ching": 69,
    "Vintareh": 90,
    "Lavy": 84,
    "Vokeh": 73
}

student_grades = dict()

# Accessing marks
for student in student_marks:
    marks = student_marks[student]

    if marks > 90:
        student_grade[student] = "A"
    elif marks > 80:
        student_grade[student] = "B"
    elif marks > 70:
        student_grade[student] = "C"
    else:
        student_grade[student] = "Pass"

print(student_grades)