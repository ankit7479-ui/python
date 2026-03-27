
#custom Expection 
class CustomError(Exception):
    pass

try:
    raise CustomError("An error is occurring...")
except CustomError as e:
    print(e)
    

