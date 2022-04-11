from stack_and_queue.queue import Queue

class Dog():
    def __init__(self):
        self.animal_type = "dog"

    def __str__(self):
        return self.animal_type
    
class Cat():
    def __init__(self):
        self.animal_type = "cat"

    def __str__(self):
        return self.animal_type

class Frog():
    pass
class AnimalShelter:
    """
    A class which holds cats and dogs
    """
    def __init__(self):
        self.animals_shelter = Queue()

    def enqueue(self,animal):
        """
        Arguments: animal (Dog or Cat objects)
        """
        if isinstance(animal,Dog) or isinstance(animal,Cat):
            self.animals_shelter.enqueue(animal)
        else:
            # raise Exception("Shelter can only contain Cats and Dogs")
            return "Shelter can only contain Cats and Dogs"

    def dequeue(self,pref):
        """
        Arguments: prefrence ("Dog" or "Cat")
        Returns: "Dog" or "Cat" or "None"
        """
        pref = pref.lower()
        if self.animals_shelter == None:
            raise Exception("Shelter is Empty")
        elif pref != "dog" and pref != "cat":
            raise Exception("Shelter only contains Cats and Dogs")
        else:
            current = self.animals_shelter.front
            temp_current = self.animals_shelter.front
            temp_current_next = temp_current.next
            while temp_current and temp_current_next:
                if str(temp_current.value) != pref:
                    temp_current = temp_current.next
                    temp_current_next = temp_current_next.next
                elif str(temp_current.value) == pref:
                    prev_current = current.value
                    self.animals_shelter.front.value = temp_current.value
                    # print("before dequeue",self.animals_shelter.to_string())
                    temp_current.value = prev_current
                    temp_current_next = temp_current_next.next
                    self.animals_shelter.dequeue()
                    # print("after dequeue",self.animals_shelter.to_string())
                    return str(current.value)  
            else:
                return "Animal is currently unavailable in the shelter"

    def to_string(self):
            queue_str = ""
            if self.animals_shelter.front == None:
                queue_str = "Shelter is empty"
            else:
                current = self.animals_shelter.front
                while current:
                    queue_str += "{ " + str(current.value) + " }" + " -> "
                    current = current.next
                queue_str += "None"
            return queue_str

if __name__ == "__main__":
    from queue import Queue
    # dog = Dog()
    # print(dog)
    # cat = Cat()
    # print(cat)
    shelter = AnimalShelter()
    # shelter.enqueue(Frog())
    
    shelter.enqueue(Dog())
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    shelter.enqueue(Cat())
    shelter.enqueue(Dog())
    print("enqueue",shelter.to_string())

    print(shelter.dequeue("cat"))
    # print(shelter.dequeue("dog"))

    print(shelter.to_string())
