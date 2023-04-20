class item:
    def __init__(self,name,price,quantity,color) :
        self.name = name
        self.price = price
        self.quantity = quantity
        self.color = color
    
    def cost(self):
        print(self.price * self.quantity)
    
    def printing(self):
        print(f'Name : {self.name}')
        print(f'Price : {self.price}')
        print(f'Color : {self.color}')


        
    







#driver code
Item1 = item('Car',1000,1,'red')
Item1.printing()
Item1.cost()
