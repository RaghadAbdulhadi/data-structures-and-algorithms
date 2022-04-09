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
