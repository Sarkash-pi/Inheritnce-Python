class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def speak(self):
        return f'My name is {self.name}'

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age) # we use this super() intead self.name/ age 

    # we override the superclass by caling a method in this def
    def speak(self):
        return 'whoof whoof!'


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)