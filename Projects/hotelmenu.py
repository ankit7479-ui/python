
menu = {
    'Pizza' : 40,
    'Dosa' : 30, 
    'pasta' : 40,
    'coffee': 15,
    'Tea': 10
}

# Greet 
print("Welcome to Python restaurant")
print("Pizza: Rs40\nDosa: Rs40\npasta:Rs40\ncoffee:Rs30\nTea:Rs20")

order_total = 0
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu :
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not avaialable yet")
    
another_order = input("Do you have another item? (Yes/No)")   
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ") 
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Item {item_2} is not available") 
        
        
print(f"The total amount of item to pay is {order_total}")        
