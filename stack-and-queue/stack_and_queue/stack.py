class Node:
    """
    A class that represents individual elements in a stack
    """
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    """
    A class that instantiate, push, pop, peek, and check if stack is empty
    """
    def __init__(self):
        self.top = None

    def push(self,value):
        """
        A function that adds a new node with that value to the top of the stack with an O(1) Time performance.
        Arguments: value
        Returns: The stack with the new node added
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """
        A function that removes node from the top of the stack
        Arguments: none
        Returns: The value from node from the top of the stack
        """
        if self.top is None:
            return "Stack is empty"
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value

    def peek(self):
        """
        A function that takes no arguments and returns the top value
        Arguments: none
        Returns: Value of the node located at the top of the stack
        """
        if self.top is None:
            return "Stack is empty"
        return self.top.value

    def is_empty(self):
        """
        A function that takes no arguments and returns a boolean
        Arguments: none
        Returns:  Boolean indicating whether or not the stack is empty
        """
        if self.top is None:
            return True
        return False

    def to_string(self):
            stack_str = ""
            if self.top == None:
                stack_str = "Stack is empty"
            else:
                current = self.top
                while current:
                    stack_str += "{ " + str(current.value) + " }" + " -> "
                    current = current.next
                stack_str += "None"
            return stack_str

if __name__ == "__main__":
    stack = Stack()
    stack.push("Raghad")
    stack.push("Jood")
    print(stack.to_string())
    