class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Cat(Animal):
    def meow(self):
        print(self.name, "says meow")

my_cat = Cat("whiskers")
my_cat.eat()
my_cat.meow()