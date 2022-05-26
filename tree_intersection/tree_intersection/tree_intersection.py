from trees import BinaryTree, Node
from hashtable import Hashtable


class MyException(Exception):
    pass

def tree_intersection(tree_one, tree_two):
    """
    A function that takes in two trees as parameters, and using Hashmap implementation as a part of the algorithm, it returns a set of values found in both trees.
        Arguments: two binary trees
        Returns: set of values found in both trees
    """
    if not tree_one.root or not tree_two.root:
        raise MyException("One of the trees or both is empty")
    hash_table = Hashtable()
    values_set = set()
    def walk(node, tree_num):
        nonlocal values_set
        if node:
            hashed_key = hash_table.hash(str(node.value))
            hash_table.set(str(node.value), tree_num)
        if node.right:
            walk(node.right, tree_num)
        if node.left:
            walk(node.left, tree_num)
        if len(hash_table.table[hashed_key]) > 1 and hash_table.table[hashed_key][1][1] == 2:
            values_set.add(hash_table.table[hashed_key][1][0])
    walk(tree_one.root, 1)
    walk(tree_two.root, 2)
    if len(values_set) == 0:
        raise MyException("No common values")
    return values_set


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
