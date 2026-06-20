# zookeeper.py
class ZooKeeper:
    def __init__(self, name):
        self.name = name
    def feed_animal(self, animal):
        print(f"{self.name} feeds {animal.name}")
    def put_to_sleep(self, animal):
        print(f"{self.name} puts {animal.name} to sleep")