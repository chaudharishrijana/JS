#LOOP
# you can used for loop to iterte through a sequence like list, tuple or string[iterables]
# range function is used to generate a sequence of number
#Write a program to print multiplication table of a given number using for loop/while loop


number = int(input("Enter a number:"))
print(f" multiplication of {number} is : \n")

# when using range(start, stop)
for i in range(1, 10):
    print(f"{number} * {i} = {number * i}")



num = int(input("Enter a number: "))
print(f"Multiplication of {num}:\n")

i = 1
while i <= 10:
    print(f"{num} * {i} = {num * i}")
    i += 1

   







""" Write a program to greet all the person names stored in a list 'l' and which starts
with S."""


l = ["Siri", "Harry", "Mahi", "Sayam", "Sudhir", "Sohan", "Rabi", "David"]


for name in l:
    if name.startswith("S"):
        print(f"Hello! Good afternoon {name}")




# for loop with else  : if the code is to be executed when the loops exhausts
# break statement is used to come out of the loop when encountered and also instucts the program to exit the loop now immediately
# continue statement : to stop the current iteration of the loop and continue with the next one and instucts the program to skip this iteration
#pass statement : pass is a null statement in python and instructs to do nothing



""" Write a program to find whether a given number is prime or not. """


n = int(input("Enter a number: "))

if n <= 1:
    print("Not a prime number.")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number.")
            break
    else:
        print("Prime number.")




""""Write a program to find the sum of first n natural numbers using while loop."""



n1 = int(input("Enter a natural number: "))

i = 0
while i <= n1:
    sum = n1 + i
    i += 1

print(f"sum of first {n1} natural number {sum}")



"""  Write a program to calculate the factorial of a given number using for loop. """


nums = int(input("Enter a number: "))
factorial = 1
for i in range(1, nums +1):
    
    factorial *= i
print(f"factorial of {nums} is {factorial}")



""". Write a program to print the following star pattern.
 *
***
***** for n = 3  """

s = int(input("Enter the number of rows: "))

for i in range(1, s+1):
    print(" " * (s-i), end="")
    print("*" * (2 * i - 1))



"""  Write a program to print the following star pattern.
* * *
*   * for n = 3
* * *   """

n = int(input("Enter the size of the square (n): "))

for i in range(n):
    for j in range(n):
        
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print() 



"""  0. Write a program to print multiplication table of n using for loops in reversed
order. """

x = int(input("Enter a number: "))

print(f"\nMultiplication table of {x} in reverse order:\n")

for i in range(10, 0, -1):
    print(f"{x} x {i} = {x * i}")
