#map,filter,reduce
from functools import reduce
from datetime import datetime
#map
numbers = [1,2,3,4,5]
squared = list(map(lambda x:x**2,numbers))
print(squared)

#filter
even_numbers = list(filter(lambda x:x % 2 == 0,numbers))
print(even_numbers)

#reduce
product = reduce(lambda x,y: x*y,numbers)
print(product)

#dateandtime
now = datetime.now()
print(now)

# Format date and time
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)