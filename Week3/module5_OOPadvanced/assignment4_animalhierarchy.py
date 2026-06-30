class Animal:
    def __init__(self,name,age,colour):
        self.name=name
        self.age=age
        self.colour=colour
    def display(self):
        print(self.name,self.age,self.colour)
    def sound(self):
        print("Animal sound")
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def __init__(self,name,age,colour,breed):
        super().__init__(name,age,colour)
        self.breed=breed
    def display(self):
        super().display()
        print(self.breed)
    def sound(self):
        print("Barks")
    def eat(self):
        print("Eats chicken")

class Cat(Animal):
    def __init__(self,name,age,colour,eyecolour):
        super().__init__(name,age,colour)
        self.eyecolour=eyecolour
    def display(self):
        super().display()
        print(self.eyecolour)
    def sound(self):
        print("Meowww")
    def eat(self):
        print("Drink Milk")

dg=Dog("Dimple",6,"White","normalbreed")
ct=Cat("Sweety",4,"White","brown eyes")
animal=[dg,ct]
for ani in animal:
    ani.display()
    ani.sound()
    ani.eat()