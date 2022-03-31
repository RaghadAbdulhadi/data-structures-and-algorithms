from stack_and_queue.stack_queue_animal_shelter import AnimalShelter,Dog
from stack_and_queue.queue import Queue
def test_enqueue():
    dog = Dog()
    animal = AnimalShelter()
    animal.enqueue(dog)
    actual = animal
    expected = "Dog"
    assert actual == expected