class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def sound(self):
        print("grrr!")


class Cat(Animal):
    def sound(self):
        print("purrr")


class Dog(Animal):
    def sound(self):
        print("bark!")


felix = Cat("felix", 4)
print(felix.color)
