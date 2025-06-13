#dictionary contain key_value pair


programmer = {'name': 'Lady Ada',
              'age': '89',
              'gender': 'female',
              'email': 'lady89@gmail.com',
              'phone_no.': '8899282779',
              'address': 'London',
              }


print(programmer)


# you can make a list in the dictionary 

programmerr = {'name': 'Lady Ada',
              'age': '89',
              'gender': 'female',
              'email': 'lady89@gmail.com',
              'phone_no.': '8899282779',
              'address': 'London',
              'education':['BCT','Master in datascience']
              }

print(programmerr)


# for retrieving data from dictionary we can use get method 
print(programmerr.get('name'))
print(programmerr.get('course'))

# You can use del to delete key from dictionary

del programmerr['email']



# you can pop any value than you can use like this 
age = programmerr.pop('age')
print(programmerr)
print(age)

# if you want to know all the values and keys that dictionary consist than you can do loke this

print(programmerr.keys())
print(programmerr.values())

# you can access both key and value from dictionary like this also 
for key, value in programmerr.items():
    print(key, value)