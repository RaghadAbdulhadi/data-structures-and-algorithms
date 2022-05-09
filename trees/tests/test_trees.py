import unittest
from trees.trees import Node, BinaryTree, breadth_first, tree_fizz_buzz, MyException

# Tests for the previous Challenges in the test_trees#1 file

# Max Element Tests
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

# Breadth First Tests
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

# FizzBuzz Tests
def test_correctly_replaced():
    tree = BinaryTree(Node(25))
    tree.root.left = Node(1)
    tree.root.right = Node("1")
    tree.root.right.right = Node(15)
    tree.root.left.right = Node(5)
    tree.root.left.left = Node(3)
    tree.root.right.left = Node(8)
    expected = len(tree_fizz_buzz(tree))
    actual = len(tree.pre_order_traversal())
    assert actual == expected

def test_fizz():
    tree = BinaryTree(Node(9))
    actual = tree_fizz_buzz(tree)[0]
    expected = "Fizz"
    assert actual == expected

def test_buzz():
    tree = BinaryTree(Node(25))
    actual = tree_fizz_buzz(tree)[0]
    expected = "Buzz"
    assert actual == expected

def test_fizzbuzz():
    tree = BinaryTree(Node(15))
    actual = tree_fizz_buzz(tree)[0]
    expected = "FizzBuzz"
    assert actual == expected

def test_string_number():
    tree = BinaryTree(Node("25"))
    actual = tree_fizz_buzz(tree)[0]
    expected = "Buzz"
    assert actual == expected

def test_retruns_string_num():
    tree = BinaryTree(Node(1))
    actual = tree_fizz_buzz(tree)[0]
    expected = "1"
    assert actual == expected


class EmptyTree(unittest.TestCase):

    def test_empty_tree(self):
        tree = BinaryTree()
        self.assertRaises(MyException, tree_fizz_buzz, tree)