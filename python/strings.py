#string 
"""message = "msg"
print(message)   """



#for writing in multiple line code you can use triple quotation
msg = """Hey! I am learning python. 
Do you wanna join me ?
If we learn together than we can learn easily anything and also solve lots of question easily. """
#print(msg)


# to find length of string you can use len 

#print(len(msg))

# to print any single character or whatever word or message you want you can use index which is written in square bracket []
# the number written in the square braces they are index of string written and before column : indicates from where the strings begin and and after the column : that indicates the ending of string 

""""
print(msg[5])
print(msg[4:10])
print(msg[4:]) 
print(msg[:10])
"""

# to make message in either lowercase or uppercase , you can you use lower or upper respectively 
"""
print(msg.upper())
print(msg.lower()) """

#  if you want to count a single character or a word from string than you can use .count() than it will provide how many times the character appear in it and also help to count the word how many time the word appear in it
"""
print(msg.count('learn'))
print(msg.count('l'))    """


# if you want to replace character or word from the string you can use the replace(' ',' ')  first quotation represent which you want to remove from the given string and second quotation represent which you to add in the string
"""
print(msg.replace('python','datascience'))
print(msg.replace('datascience','python'))

"""

# to add variables you can use plus symbol '+'  

greeting = "Hey"
nick_name = "Siri"
""""
message = greeting + nick_name
message = greeting + '!' + nick_name

print(message)
"""

#  here we can use .format() and f'' string method you can see the how they use actually :

# you can also use .format method also 
message = '{}, {}. Whats up?'.format(greeting, nick_name)
#  you can use f string at the begining 
message = f'{greeting}, {nick_name}. Whats up?'



print(message)



# dir is used to know what we can actually do with  the strings assign in the given variables
print(dir(greeting))
print(help(str))