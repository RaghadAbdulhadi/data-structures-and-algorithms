# Stacks and Queues
**Stack** is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.

**Queue** is a linear data structure that stores items in a First-In/First Out(FIFO) manner.

## Challenge
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
- Create a Stack class that has a top property. It creates an empty Stack when instantiated.

        Methods: Push, Pop, Peek, Is Empty 

- Create a Queue class that has a front property. It creates an empty Queue when instantiated.

        Methods: Enqueue, Dequeue, Peek, Is Empty

- Tests:

**Stack**

    1. Can successfully push onto a stack
    2. Can successfully push multiple values onto a stack
    3. Can successfully pop off the stack
    4. Can successfully empty a stack after multiple pops
    5. Can successfully peek the next item on the stack
    6. Can successfully instantiate an empty stack
    7. Calling pop or peek on empty stack raises exception

**Queue**

    8. Can successfully enqueue into a queue
    9. Can successfully enqueue multiple values into a queue
    10. Can successfully dequeue out of a queue the expected value
    11. Can successfully peek into a queue, seeing the expected value
    12. Can successfully empty a queue after multiple dequeues
    13. Can successfully instantiate an empty queue
    14. Calling dequeue or peek on empty queue raises exception

## Approach & Efficiency

**Stack Approach:**

1. Create a node class to instantiate the nodes in a stack
    2. The node class contains value and a pointer to the next node
3. Create a Stack class that instantiate a nodes top value with None
    4. Create a method that pushes the nodes into the stack
        5. Create a node using the node class
        6. Assign the next of the node to be the top pf the stack
        7. Reassign the top of the stack to be the newly added node
    8. Create a method that pops out nodes from the top of the stack
        9. If the top value is None then the stack is empty and return the stack is empty
        10. If the top is not None, assign the top node to a new varaible, reassign the top to be the next, then change the next of the assigned variable to be pointing to None, return the popped node value
    11. Create a method that returns the top value of the stack
        12. If the top value is None, return Stack is empty
        13. If not None, return the top value of the stack
    14. Create a method that checks is the stack is empty
        15. If top is None -> True
        16. If top is not None -> False

**Queue Approach:**

1. Create a node class to instantiate the nodes in a queue
    2. The node class contains value and a pointer to the next node
3. Create a Queue class that instantiate a nodes front and rear values with None
    4. Create a method that enqueues the nodes into the queue from the rear
        5. Create a node using the node class
        6. If the front value is None, assign the front and the rear to be the new node
        7. If the queue is not empty, assign rear to be pointing to the new node and reassign the rear to be the new node
    8. Create a method that dequeues out nodes from the front of the queue
        9. If the front value is None then the queue is empty and return the queue is empty
        10. If the front is not None, assign the front node to a new varaible, reassign the front to be the next, then change the next of the assigned variable to be pointing to None, return the dequeued nodes value
    11. Create a method that returns the front value of the queue
        12. If the front value is None, return Queue is empty
        13. If not None, return the front value of the queue
    14. Create a method that checks is the queue is empty
        15. If front is None -> True
        16. If front is not None -> False

**Stack**
- Push *O(1)*
- Pop *O(1)*
- Peek *O(1)*
- Is Empty *O(1)*

**Queue**
- Enqueue *O(1)*
- Dequeue *O(1)*
- Peek *O(1)*
- Is Empty *O(1)*

## API

**Stack Methods:**

*Push*

    A function that adds a new node with that value to the top of the stack with an O(1) Time performance.
    Arguments: value
    Returns: The stack with the new node added

*Pop*

    A function that removes node from the top of the stack
    Arguments: none
    Returns: The value from node from the top of the stack

*Peek*

    A function that takes no arguments and returns the top value
    Arguments: none
    Returns: Value of the node located at the top of the stack

*Is Empty*

    A function that takes no arguments and returns a boolean
    Arguments: none
    Returns:  Boolean indicating whether or not the stack is empty


**Queue Methods:**

*Enqueue*

    A function that adds the node from the rear of the queue
    Arguments: value
    Returns: The queue with the new node added

*Dequeue*

    A function that removes the node from the front of the queue
    Arguments: none
    Returns: the value from node from the front of the queue

*Peek*

    A function that takes no arguments and returns the front value
    Arguments: none
    Returns: Value of the node located at the front of the queue

*Is Empty*

    A function that takes no arguments and returns a boolean
    Arguments: none
    Returns:  Boolean indicating whether or not the queue is empty
