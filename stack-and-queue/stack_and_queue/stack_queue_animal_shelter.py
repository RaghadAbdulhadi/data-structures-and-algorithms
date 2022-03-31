from stack_and_queue.queue import Queue

class Dog():
    def __init__(self):
        self.animal_type = "Dog"
    def __str__(self):
        return f"Animal Type: {self.animal_type}"

class Cat():
    def __init__(self):
        self.animal_type = "Cat"
    def __str__(self):
        return f"Animal Type: {self.animal_type}"

class AnimalShelter():
    def __init__(self):
        self.dog = Dog()
        self.cat = Cat()
        self.shelter = Queue()

    def enqueue(self, animal):
      self.shelter.enqueue(animal)

    # def dequeue(self, pref):
    #     if pref.value == "cat":
    #         return "cat"
    #     elif pref.value == "dog":
    #         return "dog"
    #     return None

    def __str__(self):
        return f"Current AnimalShelter = {self.shelter}"

if __name__ == "__main__":
    from queue import Queue
    first_animal = Dog()
    print(first_animal)
    second_animal = Cat()
    print(second_animal)
    add_animal = AnimalShelter()
    add_animal.enqueue(first_animal)
    print(add_animal)
