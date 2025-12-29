class Animal:
    # this is my test
    alive = set()
    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.add(self)
    
    def __repr__(self):
        return (f"name: {self.name}, health: {self.health}, hidden: {self.hidden}")

class Herbivore(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def hide(self):
        self.hidden = True

        self.hidden = not self.hidden


class Carnivore(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    def bite(self, animal: Animal) -> None:
        if animal in Animal.alive and not animal.hidden:
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)
