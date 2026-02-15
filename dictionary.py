info = {
    "name": "Rohit",
    "age": 22,
    "Student": True,
    "subject": ["cs","loop",45]
}


info["name"] = "Harsh"  # dicionary is mutable


print(info)

# Nested Dictionary 

student={
    "name":"rohit",
    "scores" : {
        "chem": 68,
        "math":98,
        "phc":78
    },
    "grade":"A"
}


print(student["scores"] ["chem"]) # to print nested value


# methods of Dictionary
print(student.keys()) # To get the Keys of Dictionary

print(student.items()) #To get the key:value pairs

print()


