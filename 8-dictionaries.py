person = {
    "first_name": "Guilherme",
    "last_name": "Bim",
    "age": 26,
    "country": "Brazil",
    "is_marred": False,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
print(len(person))
print(person["first_name"])
print(person["country"])
print(person["skills"])
print(person["skills"][0])
print(person["address"]["street"])
print(person["city"])
person["job_title"] = "Instructor"
person["skills"].append("HTML")  # add
print(person)

dct = {"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"}
print(len(dct))

# check and removing
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) 
print('key5' in dct) 


dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') 
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() 
del dct['key2'] 

person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item

#change dict to list
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) 

# clear
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

del dct

#Copy
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() 

# dict as a list
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     

#dict values as a list
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     
