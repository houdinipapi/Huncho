travel_data = {
    "Parks": ["Amboseli", "Ruma", "Tsavo", "Nairobi"],
    "Lakes": ["Victoria", "Baringo", "Naivasha", "Nakuru"],
}

print(travel_data)
print(travel_data["Lakes"][3])  # prints Nakuru

student_data = [
    {
        "Name": "Papi",
        "Age": 34,
        "Language": "Python"
    },
    {
        "Name": "Houdini",
        "Age": 45,
        "Language": "JavaScript"
    }
]

print(student_data)
# Printing Houdini's age
print(student_data[1]["Age"])