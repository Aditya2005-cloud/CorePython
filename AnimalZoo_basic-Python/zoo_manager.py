# zoo_manager.py
class Zoo:
    def __init__(self):
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} added to zoo")
    def remove_animal(self, animal):
        self.animals.remove(animal)
        print(f"{animal.name} removed from zoo")
    def show_all_animals(self):
        print("\nZoo Animals:")
        for animal in self.animals:
            print(animal.name)