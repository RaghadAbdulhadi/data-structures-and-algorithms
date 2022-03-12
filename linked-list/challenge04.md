# Singly Linked List

Linked List is a linear data structure. 
Unlike arrays, linked list elements are not stored at a contiguous location, the elements are linked using pointers.

**Parts of linked lists**

1. Values of the node.
2. The address of the next node.

**Traversal**

We depend on the Next value in each node to guide us where the next reference is pointing. The Next property is exceptionally important because it will lead us where the next node is and allow us to extract the data appropriately.

**Benfits:**

1. No need to preallocate space
2. Insertion is easier

## Challenge

Create a linked list by creating a Node class and a linked list class.
Node Class: A class that represents individual elements in a linked list
Linked list class: A class that instantiate, insert at the begining, insert at the end, removes nodes from a linked list and get the length of the list and checks if it contains a specific value.

## Approach & Efficiency

- Insert/Delete Element at the beginning = O(1)
- Insert/Delete Element at the end = O(n)
- Insert Element at the middle = O(n)

- Linked list Traversal = O(n)
- Accessing Element by value = O(n )

## API

**Insert:**

A function that adds a new node with the value to the the begining of the list, with O(1) time performance.

    Arguments: value
    Returns: Nothing

**Includes:**

A function that indicates whether the value exists as a Node's value.

    Arguments: value
    Returns: Boolean

**To String:**

A function that takes no arguments and returns a formatted string.

    Arguments: none
    Returns: String representation of the values in the linked list.

        "{ a } -> { b } -> { c } -> None"