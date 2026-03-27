""" slicing Operation 
numbers = [1,2,3,4]
print(numbers[1:4])

 Comprehension Operation
squares = [x**3 for x in range(5)]
print(squares)

Sorting and Reversing
numbers = [9,6,8,7,1]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)"""

#Advances
#Dict
names = ["Alice","Bob","Yash"]
ages = [22,23,24]
age_dict = {name: age for name, age in zip(names, ages)}
print(age_dict)

#List
numbers = [2,3,4,5,6]
squares = [x**2 for x in numbers]
print(squares)

#Enumerate:
fruits = ["apple","Orange","Mangoe"]
for index, fruit in enumerate(fruits):
 print(f"{index}:{fruit}")
 
#Zip
names = ["Alice","Bob","Yash"]
scores =[60,80,60]
combined = zip(names,scores)
print(list(combined))