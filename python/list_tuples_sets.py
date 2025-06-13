#list
# if you want to make list you can use square braces

students = ['name', 'roll_no', 'age', 'class']
print(students)
# you can use index also in it 
print(students[-3])

# if you want to add value in the list you can use append 
students.append('marks')
print(students)

# if you want insert any value whereever you want you can use indices also


students.insert(4, 'faculty')
print(students)

# you can use extend to combine each value from two or more list but if you use append to combine two or more list than first list contain its values but rest of other appear in the form of list in the first list but this is not happen in the extend only  actual values appear 

student_1 = ['address', 'id']
students.extend(student_1)
print(students)

students.append(student_1)
print(students)

#if you have stack or queue you can use pop to remove values from list
student = ['name', 'roll_no', 'age', 'class']
popped = student.pop()
print(popped)
print(student)

# sort : it is used to sort values either alphabetical order, ascending or descinding order
n = [1,2,4,6,5,10,9,8,7]
n.sort()


n.sort(reverse=True)
print(n)


# if you use only in with for that it gives only list but if you use in enumerate that it also give indices also
courses = ['statistics','numpy','panda','python','datascience','bigdata']
for course in enumerate (courses):
    print(course)



# you can also do like this 
for index, course in enumerate(courses, start=1)  :
    print(index, course) 


# tuple is almost like list but in tuple we can use small braces instead of square braces

tuple_1 = ('math','physics','chemistry','biology','AI','ML')
tuple_2 = ('famework','libraries','stack','language')

print(tuple_1 + tuple_2)
print(f'{tuple_1},{tuple_2}')


# difference of list and tuple
"""
list : mutable i.e it can changable, you can modify data whenever needed  where data needed modification you can use list method add, remove
tuple : immutable i.e it can't be changed, you can't modify data whenever needed where data is no need to change than you can use tuple method count, index

"""

#sets use middle or curly braces for this 
# sets are actually what you do in math like intersection, difference, union
course = {'history','math','social','physics'}
coursess = {'math','physics','chenistry','biology','AI','ML'}
print('math' in course)
print('bio' in course)
print(course.intersection(coursess))
print(course.union(coursess))
