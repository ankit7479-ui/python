"""Fibonacci Series in Python
def fib(n):
    a,b = 0,1
    
    while a < n:
        print(a,end='')
        
        a,b = b,a + b
    print()   
    
fib(100)  """

#Fibonacci in Stock Market
def fib(n):
    a,b = 0,1
    
    series =[0,1,1,2,3,5]
    while a < n:
       series.append(a)
       a,b = b,a+b
       return series
   
max_price = 1000
retracement_levels = fib(max_price)
print("Fibonacci levels:",retracement_levels)   