class Product:
    def __init__(self,name,price,brand):
        self.name=name
        self.price=price
        self.brand=brand
    def display(self):
        print(self.name)
        print(self.brand)
        print(self.price)
    def buy(self):
        print("Product is purchased")
class Electronics(Product):
    def __init__(self,name,price,brand,warranty):
        super().__init__(name,price,brand)
        self.warranty=warranty
    def display(self):
        super().display()
        print(self.warranty)
    def buy(self):
        print("Electronics is purchased")
class Clothing(Product):
    def __init__(self,name,price,brand,size):
        super().__init__(name,price,brand)
        self.size=size
    def display(self):
        super().display()
        print(self.size)
    def buy(self):
        print("Clothing is purchased")
electronic=Electronics("TV",56000,"Samsung","4 years")
cloth=Clothing("Cotton",2000,"Max","S")
products=[electronic,cloth]
for product in products:
    product.display()
    product.buy()