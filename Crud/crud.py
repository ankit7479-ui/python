class CRUDList:
    # python list
    def __init__(self):
        self.data = []
        self.counter = 1
        
    # CREATE
    def create(self,item):
        new_item = {
            'id':self.counter,
            'data':item
        }   
        self.data.append(new_item)
        self.counter += 1
        return new_item 
    
    # READ
    def read(self,item_id=None):
        if item_id is None:
          return self.data
        else:
          for item in self.data:
            if item['id'] == item_id: 
                return item
            return None      
     
#Update 
    def update(self,item_id,new_data):
     for item in self.data:
        if item['id'] == item_id:
            item['data'] = new_data
            return item
        return None
  
# delete
    def delete(self,item_id):
       for i,item in enumerate(self.data):
         if item['id'] == item_id:
             return self.data.pop(i)
         return None

      # Display all items
    def display(self):
        for item in self.data:
            print(f"ID: {item['id']}, Data: {item['data']}")
 
 
print("=" * 50)
print("CRUD with Lists")
print("=" * 50) 

crud = CRUDList()
  
#create
print("\n1. CREATE Operations:")  
crud.create("Apple") 
crud.create("Mangoe") 
crud.create("cherry")
crud.display()

#Read
print("\n2. Read Operation")
print("All item:",crud.read())
print("Item with ID 2:", crud.read(2))

#update
print("\n3. Update Operations ")
crud.update(2,"Blueberry")
crud.display()

#delete
print("\n4. Delete Operation")
crud.delete(1)
crud.display()