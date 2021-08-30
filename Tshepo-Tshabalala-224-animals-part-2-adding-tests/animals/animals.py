class Animals():
    def eats(self):
        return "Food"

    def sounds(self):
        return "..."
        
class Dog(Animals):
    def __init__(self):
        self.name = "Rax"

    def sounds(self):
        return "Bark"

class Cat(Animals):
    def __init__(self):
        self.name = "Stormy"

    def sounds(self):
        return "Meow"

class Home():
    def __init__(self):
        self.pet = []

    def adopt_pet(self, animal):
        if animal in self.pet:
            raise ValueError('Not okay at all')
        else:
            self.pet.append(animal)
            print('totally okay')

    def make_all_sounds(self):
        for i in self.pet:
            print(i.sounds())