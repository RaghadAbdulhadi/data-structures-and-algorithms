from trees.trees import Node, BinaryTree, breadth_first
from trees.queue import Queue
def test_max_element():
    tree = BinaryTree(Node(4))
    tree.root.left = Node(2)
    tree.root.right = Node(55)
    tree.root.right.right = Node(6)
    tree.root.left.right = Node(30)
    tree.root.left.left = Node(1)
    tree.root.right.left = Node(11)
    actual = tree.max_element()
    expected = 55
    assert actual == expected

def test_max_element_at_end():
    tree = BinaryTree(Node(4))
    tree.root.left = Node(2)
    tree.root.right = Node(55)
    tree.root.right.right = Node(6)
    tree.root.left.right = Node(30)
    tree.root.left.left = Node(1)
    tree.root.right.left = Node(1001)
    actual = tree.max_element()
    expected = 1001
    assert actual == expected

def test_breadth_first():
    tree = BinaryTree(Node(4))
    tree.root.left = Node(1)
    tree.root.right = Node(12)
    tree.root.right.right = Node(16)
    tree.root.left.right = Node(2)
    tree.root.left.left = Node(0)
    tree.root.right.left = Node(8)
    actual = breadth_first(tree)
    expected = [4, 1, 12, 0, 2, 8, 16]
    assert actual == expected

def test_only_root_breadth_first():
    tree = BinaryTree(Node(4))
    actual = breadth_first(tree)
    expected = [4]
    assert actual == expected

def test_no_nodes_breadth_first():
    tree = BinaryTree()
    actual = breadth_first(tree)
    expected = "Tree is empty"
    assert actual == expected

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
            return "Queue is empty"
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
            return "Queue is empty"
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
            

    
