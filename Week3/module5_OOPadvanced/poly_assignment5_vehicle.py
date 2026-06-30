class Vehicle:
    def __init__(self,brand,colour):
        self.brand=brand
        self.colour=colour
    def display(self):
        print("Brand:",self.brand)
        print("Colour:",self.colour)
    def start(self):
        print("Started")
    def stop(self):
        print("Stopped")
class Car(Vehicle):
    def __init__(self,brand,colour,doors):
        super().__init__(brand,colour)
        self.doors=doors
    def display(self):
        super().display()
        print("Doors:",self.doors)
    def start(self):
        print("Key start")
class Bike(Vehicle):
    def __init__(self,brand,colour,helmet_required):
        super().__init__(brand,colour)
        self.helmet_required=helmet_required
    def display(self):
        super().display()
        print("Helmet required:",self.helmet_required)
    def start(self):
        print("Kick start")
    
bk=Bike("RE","green",True)
cr=Car("wagonr","blue",4)
vehicles=[bk,cr]
for vehicle in vehicles:
    vehicle.display()
    vehicle.start()
    vehicle.stop()