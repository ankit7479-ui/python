class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self): 
        return f"Hello my name {self.name} and age is {self.age}"   
    
Person1 = Person("Alice",23)  
print(Person1.greet()) 