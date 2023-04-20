#working with constructor and __init__
class item: 
    laptop_discount = 0.8
    def __init__(self,name:str,price:int,color:str,quantity=0):
        self.name = name
        self.price = price
        self.color = color
        self.quantity = quantity
    
    def pay(self):
        return (self.quantity * self.price)
    def discount(self):
        self.price=  self.price*self.laptop_discount

    

        





#driver code 
item1 = item('Mobile',1000,'Red',10)

print('Item Total Price is: ',item1.pay())
item2 = item('Laptop',1000000,'White',1)
item2.discount()
print('Laptop price is :',item2.price)
