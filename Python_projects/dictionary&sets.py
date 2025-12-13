info = {
    "Name" : "Subhash",
    "age" : 21,
    "Subject": ["account", "Economc", "science"],
 
}

info["Name"]= "Tiwari"
info["percentage"] = 90
print(info)


# Nested Dictionary

crack = {
    "user": "Subhash",
    "Subject": {
        "phy": 90,
        "chem": 98,
        "math": 96
    }
}

print(list(crack.keys()))   # Correct key

# questions solving 

dictionary = {
     "Cat": "a small animal",
     "table": ["a pecie of furniture", "list of facts & figures"]
}

print(dictionary)

subject = {
    "python", "java", "C++", "python", "javascript", "java", "python", "java", 
    "python", "java", "c++", "C"
}

print(subject)
print(len(subject))

marks = {}

x = int(input("Enter phy : "))
marks.update({"phy":x})

x = int(input("Enter math : "))
marks.update({"math":x})

x = int(input("Enter che : "))
marks.update({"che":x})

print(marks)

values = {9, 9.25, 8, "9.0"}
print(values)

values1 = {
    ("float", 9.0),
    ("int", 9)
}

print(values1)


