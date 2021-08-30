from animals.animals import Dog, Cat

class TestAnimal():
    def test_dog_sound(self):
        dog = Dog()
        assert dog.sounds() == "Bark", "The dog should Bark"

    def test_cat_sound(self):
        cat = Cat()
        assert cat.sounds() == "Meow", "The cat should Meow"

    def test_dog_eats(self):
        dog = Dog()
        assert dog.eats() == "Food", "The dog should eat Food"

    def test_cat_eats(self):
        cat = Cat()
        assert cat.eats() == "Food", "The cat should eat Food"