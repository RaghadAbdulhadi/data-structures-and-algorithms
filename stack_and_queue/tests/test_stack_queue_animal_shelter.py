from stack_and_queue.stack_queue_animal_shelter import AnimalShelter,Dog,Cat,Frog


def test_multiple_enqueue():
    shelter = AnimalShelter()
    shelter.enqueue(Dog())
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    actual = shelter.to_string()
    expected = "{ dog } -> { dog } -> { cat } -> { dog } -> { cat } -> { dog } -> None"
    assert actual == expected

def test_dequeue():
    shelter = AnimalShelter()
    shelter.enqueue(Dog())
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    shelter.dequeue("cat")
    actual = shelter.to_string()
    expected = "{ dog } -> { dog } -> { dog } -> { cat } -> { dog } -> None"
    assert actual == expected

def test_adopted_animal():
    shelter = AnimalShelter()
    shelter.enqueue(Dog())
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    actual = shelter.dequeue("cat")
    expected = "cat"
    assert actual == expected

def test_not_cat_or_dog():
    shelter = AnimalShelter()
    actual = shelter.enqueue(Frog())
    expected = "Shelter can only contain Cats and Dogs"
    assert actual == expected

def test_shelter_is_out_of_a_type():
    shelter = AnimalShelter()
    shelter.enqueue(Dog())
    shelter.enqueue(Dog())
    shelter.enqueue(Dog())
    shelter.enqueue(Dog())
    actual = shelter.dequeue("cat")
    expected = "Animal is currently unavailable in the shelter"
    assert actual == expected