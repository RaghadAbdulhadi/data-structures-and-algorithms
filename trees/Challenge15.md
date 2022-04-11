# Trees
A Tree is a Data structure in which data items are connected using references in a hierarchical manner. Each Tree consists of a root node from which we can access each element of the tree.

The topmost node is called root of the tree. The elements that are directly under an element are called its children. The element directly above something is called its parent.

**Why Trees?**

- One reason to use trees might be because you want to store information that naturally forms a hierarchy.
- Access/search quicker than Linked List and slower than arrays.
- Insertion/deletion quicker than Arrays and slower than Unordered Linked Lists
## Challenge
**Node Class**

Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

**Binary Tree Class**

Define a method for each of the depth first traversals:
- pre order which returns an array of the values, ordered appropriately.
- in order which returns an array of the values, ordered appropriately.
- post order which returns an array of the values, ordered appropriately.

**Binary Search Class**
A subclass of the Binary class with the following methods:
*Add*

    A method that adds a new node with that value in the correct location in the binary search tree.
        Arguments: value
        Return: nothing

*Contains*

    A method that checks whether or not the value is in the tree at least once.
        Argument: value
        Return: boolean
## Approach & Efficiency
**Approach**

*Pre Order*
- Check if the current node is empty / null.
- Display the data part of the root (or current node).
- Traverse the left subtree by recursively calling the pre-order function.
- Traverse the right subtree by recursively calling the pre-order function.

*In Order*

- Check if the current node is empty / null.
- Traverse the left subtree by recursively calling the in-order function.
- Display the data part of the root (or current node).
- Traverse the right subtree by recursively calling the in-order function.

*Post Order*
- Check if the current node is empty / null.
- Traverse the left subtree by recursively calling the post-order function.
- Traverse the right subtree by recursively calling the post-order function.
- Display the data part of the root (or current node).

**Big O**
Space Complexity: O(log(n))
Time Complexity: O(log(n))
## API
**Binary Tree**

*Pre Order*

    Root -> Left -> Right
    Arguments: None
    Return: list of the values, ordered appropriately

*In Order*

    Left -> Root -> Right
    Arguments: None
    Return: array of the values, ordered appropriately

*Post Order*
    Left -> Right -> Root
    Arguments: None
    Return: array of the values, ordered appropriately

**Binary Search Tree**

*Add*

    A method that adds a new node with that value in the correct location in the binary search tree.
        Arguments: value
        Return: nothing

*Contains*

    A method that checks whether or not the value is in the tree at least once.
        Argument: value
        Return: boolean
