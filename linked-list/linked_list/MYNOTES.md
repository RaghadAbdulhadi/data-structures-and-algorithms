# Linked Lists

Benfits:
1. No need to preallocate space
2. Insertion is easier

**Big O notation:**
Insert/Delete Element at the beginning = O(1)
Insert/Delete Element at the end = O(n)
Insert Element at the middle = O(n)

Linked list Traversal = O(n)
Accessing Element by value = O(n)

Array vs Link list:
![Array vs Link list](../images/arrayVslinked.PNG)

**Space**

Linked lists hold two main pieces of information (the value and pointer) per node. This means that the amount of data stored increases linearly with the number of nodes in the list. Therefore, the space complexity of the linked list is linear:
​   Space - O(n)

O(1) complexity, on the other hand, allows additional space to be taken, as long as the extra space does not increase as the input size increases.

So if we remove one node from a linked list, store it somewhere, and then when we’re done with that repeat with another node, that is O(1) space complexity.


```python

```