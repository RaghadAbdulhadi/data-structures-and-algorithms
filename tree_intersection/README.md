# Challenge Summary
A function that takes in two trees as parameters, and using Hashmap implementation as a part of the algorithm, it returns a set of values found in both trees.
    Arguments: two binary trees
    Returns: set of values found in both trees
## Whiteboard Process
![tree-intersection](https://www.figma.com/file/BlY29rCU2mrSdHV5rNwHiM/Tree-Intersections?node-id=0%3A1)
## Approach & Efficiency
### Approach
- Create a function that takes in two trees and return the values found in both trees in a set, using hashmap implementation
- Check if one of the trees is empty or both, and raise and exception
- Intialize a hastable 
- Intialize a empty set
- Create a helper function to traverse over the the two trees
- If node is not none
- Create an hashed_key
- The key in the table will be depending on the tree number
- Set the value and the key in the table 
- If node’s left is not none , traverse over the next left
- If node’s right is not none , traverse over the next right
- If the length of the element in the hashed_key index is greater that 1 and its value is equal to 2, that means the value is pressent in both trees
- Add the value to the set
- Call the helper function for the two trees and pass there roots
- If the len of the ser is equal to zero -> no common values
- Raise an exceptiom
- Return the set with the common values
### Efficiency
Time Complexity: O(n)

Space Complexity: O(n)

## Solution
```python
if __name__ == "__main__":
    # Tree One
    tree_one = BinaryTree(Node(22))
    tree_one.root.left = Node(22)
    tree_one.root.left.left = Node(22)
    tree_one.root.left.right = Node(22)
    tree_one.root.left.left.left = Node(55)
    tree_one.root.left.left.right = Node(46)
    tree_one.root.left.right.left = Node(17)
    tree_one.root.left.right.right = Node(88)
    tree_one.root.right = Node(2)
    tree_one.root.right.left = Node(20)
    tree_one.root.right.right = Node(3)
    tree_one.root.right.right.right = Node(5)
    tree_one.root.right.right.left = Node(60)
    tree_one.root.right.left.left = Node(8)
    tree_one.root.right.left.right = Node(7)
    # Tree Two
    tree_two = BinaryTree(Node(1))
    tree_two.root.left = Node(20)
    tree_two.root.left.left = Node(3)
    tree_two.root.left.right = Node(44)
    tree_two.root.left.left.left = Node(55)
    tree_two.root.left.left.right = Node(46)
    tree_two.root.left.right.left = Node(17)
    tree_two.root.left.right.right = Node(88)
    tree_two.root.right = Node(2)
    tree_two.root.right.left = Node(20)
    tree_two.root.right.right = Node(3)
    tree_two.root.right.right.right = Node(5)
    tree_two.root.right.right.left = Node(60)
    tree_two.root.right.left.left = Node(8)
    tree_two.root.right.left.right = Node(7)

    print(tree_intersection(tree_one, tree_two))
# Run file
"/home/raghad/Code Challenges/data-structures-and-algorithms/trees/.venv/bin/python" "/home/raghad/Code Challenges/data-structures-and-algorithms/tree_intersection/tree_intersection/tree_intersection.py"
# Output -> 
{'3', '5', '2', '88', '7', '60', '8', '44', '20'}
```