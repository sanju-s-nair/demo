class Animal:
    def __init__(self):
        print("Animal Created")
    
    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("I am a Dog")
        Animal.whoAmI(self)

    def eating(self):
        Animal.eat(self)
        return "Waffles"
        

x = Dog()

    
