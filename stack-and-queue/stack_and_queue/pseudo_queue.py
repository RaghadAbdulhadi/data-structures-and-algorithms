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
        if self.stack_one.is_empty():
            return "Stack one is empty"
        self.stack_one.push(value)

    def dequeue(self):
        """
        A function that extracts a value from the PseudoQueue, using a first-in, first-out approach.
        Arguments: value
        Return: Nothing 
        """
        if self.stack_two.top == None:
            while self.stack_one.top != None:
                self.stack_two.push(self.stack_one.pop())
            return "Queue is empty"

    
    def to_string(self):
        queue_stack_str = ""
        if self.stack_one.is_empty():
            queue_stack_str = "Stack is empty"
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
    pseudo.enqueue("jood")
    pseudo.dequeue()

    print(pseudo.to_string())