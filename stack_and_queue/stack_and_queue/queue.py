class Node:
    """
    A class that represents individual elements in a queue
    """
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    """
    A class that instantiate, enqueue, dequeue, peek, and check if queue is empty
    """
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        """
        A function that adds the node from the rear of the queue
        Arguments: valueb
        Returns: The queue with the new node added
        """
        node = Node(value)
        if not self.front:
            self.rear = node
            self.front = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """
        A function that removes the node from the front of the queue
        Arguments: none
        Returns: the value from node from the front of the queue
        """
        if self.front == None:
            return None
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

    def peek(self):
        """
        A function that takes no arguments and returns the front value
        Arguments: none
        Returns: Value of the node located at the front of the queue
        """
        if self.front == None:
            return None
        return self.front.value

    def is_empty(self):
        """
        A function that takes no arguments and returns a boolean
        Arguments: none
        Returns:  Boolean indicating whether or not the queue is empty
        """
        if self.front is None:
            return True
        return False

    def length(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def to_string(self):
            queue_str = ""
            if self.front == None:
                queue_str = "Stack is empty"
            else:
                current = self.front
                while current:
                    queue_str += "{ " + str(current.value) + " }" + " -> "
                    current = current.next
                queue_str += "None"
            return queue_str
            

    
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue("Gheed")
    queue.enqueue("Raghad")
    queue.enqueue("Jood")
    queue.enqueue("Omar")
    queue.dequeue()
    print(queue.length())
    print(queue.to_string())
