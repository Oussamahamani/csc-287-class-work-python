from abc import ABC, abstractmethod
# Step 1: Create an abstract base class
class Shape(ABC):
    @abstractmethod	
    def area(self): 
        pass
    
    @abstractmethod	
    def perimeter(self):    
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius  
    
    def area(self):
        return 3.14*self.radius**2
    
    def perimeter(self):
        return 2 *3.14*self.radius    
    

shape1= Circle(5)   

print(shape1.perimeter())










class slot:
    init self name,products,amount
    name= "A"
    products = [PRoduct,Snack]
    
    
    
class vendingMachine:
    slots = []
    
    
    stockitem:
        sels.slots.append(Slot(location,product_list,))
        
        
    purchase("A1")
    for slot in self.slots
        ifslot.name == name
    
    
    slots ={
        "A1":{
            price,
            list
            
        }
    }
    
    
    slots["a1"]
    
    
    stockItem(name,price,list)
    
    slots[name] =Slot("")
    
    slots["a1"]["productlist"].pop()