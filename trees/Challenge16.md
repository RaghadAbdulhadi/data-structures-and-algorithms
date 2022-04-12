# Challenge Summary
A method that finds the maximum element stored in the tree and returns its value

    Arguments: None
    Returns: number

## Whiteboard Process
![Max-Tree](./images/maxtreeWB.PNG)

## Approach & Efficiency
**Approach:**

- Create a method that takes no arguments and returns the max value of the nodes in the tree

- Instaniate a max_element varaible as zero

    - Create a helper function inside the main function to go through each node in the tree recursively, takes a node as an argument, and instaniate the node with self.root as the first node

        - If self.root is None then the tree is empty
            - Return Tree has no nodes
        - If max_element is smaller that the node’s value
            - Reassign the max_element to be the node’s value
        - If node.left is not None
            - Recall the function with node.left
        - If node.right is not None
            - Recall the function with node.right

    Call the function with self.root

    Return the max_element value

**Big O:**

Time Complexity: O(n)

Space Complexity: O(1), because the algorithm uses a single variable.
## Solution
![Solution](./images/solution%231.PNG)