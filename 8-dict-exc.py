# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, and age to the dog dictionary
dog["name"] = "Thor"
dog["color"] = "Yellow"
dog["breed"] = "English Bulldog"
dog["legs"] = 4
dog["age"] = 10

print("Dog dictionary:", dog)


# 3. Create a student dictionary
student = {
    "first_name": "Guilherme",
    "last_name": "Bim",
    "gender": "Male",
    "age": 26,
    "marital_status": "Single",
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "country": "Brazil",
    "city": "Campinas",
    "address": {"street": "Space Street", "zipcode": "02210"},
}

# 4. Get the length of the student dictionary
print("Length of student dictionary:", len(student))

# 5. Get the value of 'skills' and check its data type
print("Skills:", student["skills"])
print("Data type of skills:", type(student["skills"]))

# 6. Modify the skills values by adding one or two new skills
student["skills"].append("Flask")
student["skills"].append("Cypress")
print("Updated skills:", student["skills"])

# 7. Get the dictionary keys as a list
keys_list = list(student.keys())
print("Keys:", keys_list)

# 8. Get the dictionary values as a list
values_list = list(student.values())
print("Values:", values_list)

# 9. Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("Dictionary as list of tuples:", student_items)

# 10. Delete one of the items in the dictionary 
del student["marital_status"]
print("After deleting marital_status:", student)

# 11. Delete one of the dictionaries 
del dog

