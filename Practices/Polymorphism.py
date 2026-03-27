class Cat:
    def speak(self):
        print("Meow")
        
class Dog:
    def speak(self):
        print("woof!")   
        
animals = [Cat(),Dog()]    
for animal in animals:
    animal.speak()         