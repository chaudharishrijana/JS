# function : grouping of task performing a specific task
"""
when a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what
it can be reused by the programmer in a given program any number of 

"""
# types: built in -> function already present in the python
# types: user defined function -> defined by user 


"""
. Write a program using functions to find greatest of three numbers.

"""

#define function with argument
def find_greatest(a,b,c):
    if a >= b and a >= c:
        return a
    
    elif b >= a and b >= c:
        return b
    
    else:
        return c
    

n1 = int(input("Enter first number:"))

n2 = int(input("Enter second number:"))

n3 = int(input("Enter third number:"))

  # function calling and storing result  
greatest = find_greatest(n1, n2, n3)

print(f"The greatest number is {greatest}")



# Write a python program using function to convert Celsius to Fahrenheit.

def convert(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

c = float(input("Enter the degree Celsius: "))
degree = convert(c)

print(f"{c}°C is equal to {degree}°F")


#Write a python function which converts inches to cms.

def converts(inches):
    cms = inches * 2.54
    return cms

i = float(input("Enter the inches:"))

n = converts(i)

print(f"{i} inche is equal to {n} cm.")


# Write a python function to print multiplication table of a given number.
def multiplication_table(number):
    for i in range(1,10):
         
         print(f"{number} * {i} = {number * i}")


mul = int(input("Enter the number which you want to generate the multiplication table: "))

m = multiplication_table(mul)

#Write a python function to remove a given word from a list ad strip it at the same time.

def remove_word(words_list, word_to_remove):
    # Strip all items and remove matching word
    cleaned_list = [word.strip() for word in words_list if word.strip() != word_to_remove]
    return cleaned_list


words = ["  apple", "banana  ", "  cherry ", "banana", "  orange"]
word = "banana"

result = remove_word(words, word)
print("Updated list:", result)

"""
We all have played snake, water gun game in our childhood. If you haven’t, google the
rules of this game and write a python program capable of playing this game with the
user.

"""
import random

def game_result(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'snake' and computer == 'water') or \
         (user == 'water' and computer == 'gun') or \
         (user == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "You lose!"


choices = ['snake', 'water', 'gun']


user_choice = input("Choose snake, water, or gun: ").lower()


if user_choice not in choices:
    print("Invalid input. Please choose from snake, water, or gun.")
else:
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    
    result = game_result(user_choice, computer_choice)
    print(result)
