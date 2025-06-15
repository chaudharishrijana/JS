

# conditional expression

"""
write a program to print yes when the age entered by the user is greater than or equal to 18"""


age = int(input("Enter your age :"))

if (age >= 18):
    print("yes")

else:
    print("NO")



""" Write a program to find the greatest of four numbers entered by the user"""

number = list(map(int,input("Enter four number separated by space:").split()))


if len(number) != 4:
    print("Please enter exactly four number.")

else:
    greatest = max(number)
    print("The gratest number is ", greatest)



""""Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user."""


subject1 = int(input("Enter the marks of subject1: "))
subject2 = int(input("Enter the marks of subject2: "))
subject3 = int(input("Enter the marks of subject3: "))


if(subject1 < 33 or subject2 < 33 or subject3 < 33):
    print("You are failed because your percentage in one or more subjects is less than 33.")

else:
    overall = ((subject1 + subject2 + subject3) / 300) * 100
    if overall >= 40:
        print("You are passed and your score is", overall)
    else:
        print("You are failed because your overall score is less than 40.")



"""
A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams

"""
comment = input("Enter your comment:")

spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

is_spam = False
for keyword in spam_keywords:
    if keyword in comment:
        is_spam = True
        break


if is_spam:
    print("This is a spam comment.")

else:
    print("This is not a spam comment.")



"""
Write a program to find whether a given username contains less than 10
characters or not.

"""

username = input("Enter your username: ")

if len(username) < 10 :
    print("username must be in 10 character")
   

else:
     print(username)



"""Write a program which finds out whether a given name is present in a list or not."""



name_list = ["Alice", "Bob", "Charlie", "David", "Eva"]


names = input("Enter name(s) separated by space: ").split()


found = False
for name in names:
    if name in name_list:
        found = True
        break


if found:
    print("At least one name is available in the list.")
else:
    print("None of the names are in the list.")

