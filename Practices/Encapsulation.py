class Car:
    def __init__(self,brand,speed):
        self._brand = brand
        self._speed = speed
        
    def accelerate(self,increase):
        if increase > 0:
            self._speed += increase
            
    def brake(self,decrease):
                if decrease > 0 and self._speed - decrease >= 0:
                    self._speed -= decrease
                    
    def get_speed(self):   
        return self._speed
    
    def get_brand(self):
        return self._brand             
    
    
my_car = Car("Toyota", 50)  
print(my_car.get_speed()) 
my_car.accelerate(30) 
print(my_car.get_speed()) 
my_car.brake(20) 
print(my_car.get_speed())