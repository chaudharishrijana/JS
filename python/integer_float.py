#  to find out either data is integer or float you can use type()

num = 3
print(type(num))

n = 3.5
print(type(n))


# basic arthimetic operators 

"""
addition = 3 + 4
subtraction = 4 - 3
multiplication = 3 * 8
division = 9 / 3 (it provide float number as well as integer )
floor division = 3 // 2 (it doesn't provide float value i.e remove the value after point)
exponent = 3 ** 4 (power of 3 is 4)
modulus = 3 % 2 (it gives remainder)


"""
print(3 % 2)


#  you can also use like 
num = 4
num += 5
print(num)
# output = 9 because num is assign with 4 and in the second part num said add 5 to previous value of num 

# you can also do other operation also 

#built in function  like abs, round

print(abs(-4)) # here you want to get always postive value than you can use abs
print(round(3.33, 1))  # here you can roundoff the value by using round 

# comparisons operators
"""
equal : 4 ==2
not equal : 4 != 2
greater than : 3 > 1
less than : 4 < 7
greater or equal : 4 >= 3
less or equal : 5 <= 8

"""

# caching
num_1 = 4
num_2 = 5

num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)



num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
print(num_1 + num_2)


