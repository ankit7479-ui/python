class Animal:
    def speak(self):
        print("Animal speaks")
        
class Dog(Animal):
    def speak(self):
        print("Dog bark")      
        
dog = Dog()
dog.speak()          