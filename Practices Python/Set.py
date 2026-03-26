import time
import json
import csv
# Set Operation 
#union
set1 = {1,2,3}
set2 = {4,5,6}
union_set = set1|set2
print(union_set)

#Intersection
insertSection_set = set1 & set2
print(insertSection_set)

#Diffence
difference_set = set1 - set2
print(difference_set)

#Handling Timeouts and Delays
print("Printing start")
time.sleep(2)
print("2 Second later")

#You can create decorators that accept arguments to make them more flexible.
def repeat(n):
    def decorators(func):
        def wrapper(*args,**kwargs):
            for i in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorators

@repeat(3)
def greet(name):
    print(f"Hello {name}!")
    
greet("Alice")   
        
#Handling JSON Data:
person = {"name":"Aine","age":24}
json_data = json.dumps(person)
print(json_data)
        
#Convert JSON to Python objects:
json_string =  '{"name":"Bob","age":24}'    
person = json.loads(json_string)
print(person)

#Working with CSV Files:
"""data = [["name",'age'],["alice",24],["aline",25],["Bob",26]]
with open('data.csv','r') as file:
    reader = csv.reader(file)
    for row in(reader):
        print(row) """