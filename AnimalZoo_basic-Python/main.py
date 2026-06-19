# main.py
from dog import Dog
from cat import Cat
from lion import Lion
from zookeeper import ZooKeeper
from zoo_manager import Zoo

# Create animals
dog = Dog("Bruno", 3, "Brown")
cat = Cat("Kitty", 2, "White")
lion = Lion("Simba", 5, "Yellow")

# Animal methods
dog.introduce()
dog.eat()
dog.make_sound()

print("-"*50)

cat.introduce()
cat.eat()
cat.make_sound()

print("-"*50)

lion.introduce()
lion.eat()
lion.make_sound()

# Create zookeeper
print("-"*50)

keeper = ZooKeeper("Raju")
keeper.feed_animal(dog)
keeper.feed_animal(cat)
keeper.put_to_sleep(lion)

# Create zoo
print("-"*50)

zoo = Zoo()
zoo.add_animal(dog)
zoo.add_animal(cat)
zoo.add_animal(lion)

print("-"*50)

zoo.show_all_animals()