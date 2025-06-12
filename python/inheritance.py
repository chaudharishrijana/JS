#inheritance : way of creating a new class from an existing class


#syntax:
"""
#basse class
class Employee:
#you can write your code here

#derived or child class
class programmer(Employee)

#you can write your code here


#types of inheritance:
1. single inheritance : occurs when child class inherits only a single parent class
2. multiple inheritance : occurs when the child class inherits from more than one parent classes
3. multilevel inheritance : when a child class become parent for another child class
"""

"""
 # super() method : used to access the methods of a super class in the derived class
 super().__init__()   # __init__() calls constructor of the base class
 
 # classmethod : method which is boound to the class and not the object of the class

 @classmethod
    def(cls,p1,p2):
 
 """
# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def show(self):
        print(f"2D vector is : ({self.x}, {self.y})")

    def magnitude(self):
        return(self.x **2 + self.y **2) **(1/2)


#3d vector inherits from 2d vector
class vector3d(vector2d):
    def __init__(self, x, y, z):
        super().__init__(x,y) # calling the constructor of vector2d
        self.z = z

    def show(self):
        print(f"3D vector is : ({self.x}, {self.y}, {self.z})")

    def magnitude(self):
        return (self.x **2 + self.y **2 + self.z **2) **(1/2)
    

print("Enter components for 2D Vector:")
x2 = float(input("Enter x: "))
y2 = float(input("Enter y: "))
v2 = vector2d(x2, y2)
v2.show()
print(f"2D Vector Magnitude: {v2.magnitude():.2f}")


print("\nEnter components for 3D Vector:")
x3 = float(input("Enter x: "))
y3 = float(input("Enter y: "))
z3 = float(input("Enter z: "))
v3 = vector3d(x3, y3, z3)
v3.show()
print(f"3D Vector Magnitude: {v3.magnitude():.2f}")



# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
#base class
class animals:
    def __init__(self, species):
        self.species = species

    def info(self):
        print(f"This is an animal  of species: {self.species}")

# derived class

class pets(animals):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name

    def pet_info(self):
        print(f"This pet's name is {self.name} and it's species is {self.species}")


# child class derived from above child class

class dogs(pets):
    def __init__(self, name, breed, age, height, weight):
        super().__init__("Dog", name)
        self.breed = breed
        self.age = age
        self.height = height
        self.weight = weight

    def bark(self):
        print(f"{self.name} is barking! woof woof!")

    def dog_info(self):
        print(f" A dog named {self.name} is a {self.breed} with age {self.age} having height {self.height}cm and weight {self.weight}kg")


print("Enter the dog info :")

n =input("Enter the name :")
b = input("Enter the breed :")
a = float(input("Enter the age :"))
h = float(input("Enter the height(in cm):"))
w = float(input("Enter the weighs(in kg): "))


d = dogs(n, b, a, h, w)
d.bark()
d.dog_info()

# Create a class ‘Employee’ and add salary and increment properties to it.

class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_salary(self):
        print(f"{self.name}'s current salary is Nrs.{self.salary}  ")

    def increment(self, percent):
        # e.g i am doing for 15 %

        increment_amount = (percent / 100) * self.salary
        self.salary += increment_amount
        print(f"An increment of {percent}% applied. New salary is Nrs.{self.salary:.2f} ")


name = input("Enter employee's name: ")
salary = float(input("Enter current salary : "))
emp = employee(name, salary)

emp.show_salary()

percent = float(input("Enter increment percentage:"))
emp.increment(percent)

emp.show_salary()

