# Taylor Sayson
# Dictionaries
# 12 April 2024

# Big Ideas:
# - Dictionaries are a data structure
# - Dictionaries map keys to values

# Flashback to lists
person = [
    "John",
    "23 years old",
    "4500 1023 2222 1111"
]

# Get and print the person's name
print(person[0])

print(person[-1]) # some numbers
print(person[-2]) #second last- age?


person_dict = {
    "name": "John",
    "age": "23 years old",
    "cc num": "4500 1023 2222 1111",
    "height": 190,
    "SIN number": "727 000 111",
    "weight": 75,
    "job": "teacher"
}

for key in person_dict:
    print(key, person_dict[key], sep=": ")

for key, value in person_dict.items():
    print(key, value, sep=": ")