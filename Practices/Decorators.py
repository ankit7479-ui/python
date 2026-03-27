def decorators(func):
    def wrapper():
        print("function is Calling...")
        func()
        print("After function Calling...")
    return wrapper

@decorators 
def say_hello():
    print("Hello Alice!")
    
say_hello()


