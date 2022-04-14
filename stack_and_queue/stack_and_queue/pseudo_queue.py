from stack_and_queue.stack import Stack

class PseudoQueue:
    """
     A class that utilizes two Stack instances with push, pop, and peek methods to create and manage the queue.
    """
    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()

    def enqueue(self,value):
        """
        A function that inserts value into the PseudoQueue, using a first-in, first-out approach.
        Arguments: value
        Return: Nothing 
        """
        self.stack_one.push(value)    

    def dequeue(self):
        """
        A function that extracts a value from the PseudoQueue, using a first-in, first-out approach.
        Arguments: value
        Return: The poped element
        """
        if self.stack_one.top == None:
            return "Pseudo Queue is empty"

        if self.stack_two.top == None:
            while self.stack_one.top != None:
                self.stack_two.push(self.stack_one.pop())
        return self.stack_two.pop()

    def to_string(self):
        queue_stack_str = ""
        if self.stack_two.top == None:
            queue_stack_str = "Pseudo Queue is empty"
        else:
            current = self.stack_two.top
            while current:
                queue_stack_str += "{ " + str(current.value) + " }" + " -> "
                current = current.next
            queue_stack_str += "None"
        return queue_stack_str



if __name__ == "__main__":
    from stack import Stack
    pseudo = PseudoQueue()
    pseudo.enqueue("raghad")
    pseudo.enqueue("gheed")
    pseudo.enqueue("ayman")
    pseudo.enqueue("jood")
    pseudo.dequeue()
    print(pseudo.to_string())