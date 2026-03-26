# print triangle 
n = 5
for i in range(1,n + 1):
    print("*" * i)
    
#pyramid 
n = 5
for i in range(1,n + 1):
      print(" " * (n - i) + "*" * (2 * i - 1))