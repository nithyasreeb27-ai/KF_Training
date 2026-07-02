class Animal:
    def sound(self):
        print("Animal")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.sound()

# No inheritence
# Duck typing happens here