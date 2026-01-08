'''
execersize
'''

# create dictionary to store 20 different detail about your ownself
person = {
    "name": "Divyansh parmar",
    "age": 22,
    "gender": "true",
    "dob": "30/03/2006",
    "pincode": 364001,
    "email": "divyanshparmar706@gmial.com",
    "phone": "9876543210",
    "address": "bhavnagar",
    "nationality": "Indian",
    "marital_status": "Single",
    "occupation": "deverloper",
    "company": "none",
    "education": "B.c.a",
    "hobbies": ["coding", "playing", "Music"],
    "favorite_food": "ice creeam",
    "favorite_color": "black",
    "blood_group": "O+",
    "height_cm": 175,
    "weight_kg": 70,
    "favorite_tourist_destinations": [
        "Goa",
        "america",
        "thailand",
        "Dubai",
        "austraiaya"
    ]
}

# print dictionary
print(person)

# print name, age, gender, dob
print(person['name'])
print(person['age'])
print(person['dob'])
print(person['gender'])

# add key value pair pincode into dictionary 

person.update({"pincode":364001})
print(person)

# add key value pair to store your 5 favourite touriest destination
person.update({"favorite-destinition":["goa","america","thailand","dubai","australiya"]})
print(person) 

# print all the favourite touriest destination 
print(person["favorite_tourist_destinations"])

# use update method to add new key value pair in dictionary
person.update({"hobby":"running"})
print(person)

# use update method to change existing key value pair in dictionary
person.update({"pincode":343621})
print(person)

# use pop method to remove do
person.pop("pincode")
print(person)

# use popitem item method to remove last item 
person.popitem()
print(person)

# display all keys
print(person.keys())

# display all values
print(person.values())

# copy dictionary to another dictionary using copy function 
person2 = person.copy()
print(person2)

# clear newly create dictionary.
person2.clear()
print(person,person2)

print("good byy")
