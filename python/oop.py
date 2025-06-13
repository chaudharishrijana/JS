# object  oriented programming


#it is a dry principle i.e focus on reusable code


# class : blueprint for creating object


# Create a class “Programmer” for storing information of few programmers working at Microsoft

#define class
class Programmer:
    # constructor method to initialize the programmer's details

    def __init__(self, name, age, salary):
        self.company = "Microsoft"
        self.name = name
        self.age = age
        self.salary = salary

    #method to  display programmers details
    def show_info(self):
        print(f"Company: {self.company}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")

# creating  objects of programmer class

p1 = Programmer("Alice", 24, 30000)

p2 = Programmer("Max", 23, 40000)

p3 = Programmer("Sirir", 23, 50000)


# display result for each programmer

p1.show_info()
p2.show_info()
p3.show_info()


#. Write a class “Calculator” capable of finding square, cube and square root of a number.
import math
class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return math.sqrt(self.number)
    
    # calculator menu

while True:
    print("\n===== Calculator Menu =====")
    print("1. Find Square")
    print("2. Find Cube")
    print("3. Find Square Root")
    print("4. Exit")

    choice = input("Enter your choice 1 to 4 :")

    if choice == '4':
        print("Exit")
        break
    try:
        num = float(input("Enter a number:"))
        calc = Calculator(num)

        if choice == '1':
            print(f"Sauare of {num} is {calc.square()}")


        elif choice == '2':
            print(f"Cube of {num} is: {calc.cube()}")

        elif choice == '3':
           print(f"Square root of {num} is: {calc.square_root()}")


        else:
            print("Invalid choice. Please select 1 to 4.")


    except ValueError:
        print("Invalid input. Please enter a numeric value")






#Add a static method in problem 2, to greet the user with hello.

import math

# Define Calculator class
class Calculator:

    @staticmethod
    def greet():
        print("Hello! User")

    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return self.number ** 0.5  # Or use math.sqrt(self.number)

# Greet the user once
Calculator.greet()

# Menu loop
while True:
    print("\n===== Calculator Menu =====")
    print("1. Find Square")
    print("2. Find Cube")
    print("3. Find Square Root")
    print("4. Exit")

    choice = input("Enter your choice (1 to 4): ")

    if choice == '4':
        print("Exiting the calculator. Goodbye!")
        break

    try:
        num = float(input("Enter a number: "))
        calc = Calculator(num)

        if choice == '1':
            print(f"Square of {num} is: {calc.square()}")
        elif choice == '2':
            print(f"Cube of {num} is: {calc.cube()}")
        elif choice == '3':
            print(f"Square root of {num} is: {calc.square_root()}")
        else:
            print(" Invalid choice. Please select between 1 to 4.")

    except ValueError:
        print(" Invalid input. Please enter a numeric value.")




"""Write a Class 'Train' which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways. 
"""


class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def get_status(self):
        print(f" Train: {self.name}")
        print(f" Available seats: {self.seats}")

    def get_fare_info(self):
        print(f" Fare per ticket: ₹{self.fare}")

    def book_ticket(self):
        if self.seats > 0:
            print(" Ticket booked successfully!")
            self.seats -= 1
            print(f"Remaining seats: {self.seats}")
        else:
            print(" Sorry, the train is full. No seats available.")

# Create a Train object
my_train = Train("Rajdhani Express", 1500, 5)

# Menu-driven interaction
while True:
    print("\n Indian Railways - Train Booking System ")
    print("1. Get Train Status")
    print("2. Get Fare Information")
    print("3. Book a Ticket")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        my_train.get_status()
    elif choice == '2':
        my_train.get_fare_info()
    elif choice == '3':
        my_train.book_ticket()
    elif choice == '4':
        print(" Thank you for using Indian Railways Booking System.")
        break
    else:
        print(" Invalid choice. Please select a valid option.")

