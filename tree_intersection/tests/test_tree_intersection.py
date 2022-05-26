
import unittest
from tree_intersection.tree_intersection import tree_intersection, MyException,Node,BinaryTree, Hashtable


def test_tree_intersection_empty_tree_with_collsions():
    tree_one = BinaryTree(Node(22))
    tree_one.root.left = Node(22)
    tree_one.root.left.left = Node(22)
    tree_one.root.left.right = Node(22)
    tree_one.root.left.left.left = Node(55)
    tree_one.root.left.left.right = Node(46)
    tree_one.root.left.right.left = Node(170)

    tree_two = BinaryTree(Node(1))
    tree_two.root.left = Node(20)
    tree_two.root.left.left = Node(3)
    tree_two.root.left.right = Node(44)
    tree_two.root.left.left.left = Node(55)
    tree_two.root.left.left.right = Node(46)
    tree_two.root.left.right.left = Node(170)
    tree_two.root.left.right.right = Node(88)
    actual = tree_intersection(tree_one, tree_two)
    expected = {'3', '20', '55', '1', '88', '46', '44', '17'}

def test_tree_intersection_empty_tree_without_collsions():
    tree_one = BinaryTree(Node(22))
    tree_one.root.left = Node(22)
    tree_one.root.left.left = Node(22)
    tree_one.root.left.right = Node(22)
    tree_one.root.left.left.left = Node(55)
    tree_one.root.left.left.right = Node(46)
    tree_one.root.left.right.left = Node(17)

    tree_two = BinaryTree(Node(1))
    tree_two.root.left = Node(20)
    tree_two.root.left.left = Node(3)
    tree_two.root.left.right = Node(44)
    tree_two.root.left.left.left = Node(55)
    tree_two.root.left.left.right = Node(46)
    tree_two.root.left.right.left = Node(17)
    tree_two.root.left.right.right = Node(88)
    actual = tree_intersection(tree_one, tree_two)
    expected = {'46', '1', '20', '44', '55', '170', '3'}

class EmptyTree(unittest.TestCase):
    def test_tree_intersection_empty_tree_empty_tree(self):
        tree_one = BinaryTree(Node(22))
        tree_one.root.left = Node(22)
        tree_one.root.left.left = Node(22)
        tree_one.root.left.right = Node(22)
        tree_one.root.left.left.left = Node(55)
        tree_one.root.left.left.right = Node(46)
        tree_one.root.left.right.left = Node(17)
        tree_two = BinaryTree()
        self.assertRaises(MyException, tree_intersection, tree_one, tree_two)
    def test_tree_intersection_empty_tree_two_empty_trees(self):
        tree_one = BinaryTree()
        tree_two = BinaryTree()
        self.assertRaises(MyException, tree_intersection, tree_one, tree_two)

    def test_tree_intersection_no_common_values(self):
        tree_one = BinaryTree(Node(29))
        tree_one.root.left = Node(23)
        tree_one.root.left.left = Node(12)
        tree_one.root.left.right = Node(9)
        tree_two = BinaryTree(Node(2))
        tree_two.root.left = Node(6)
        tree_two.root.left.left = Node(8)
        tree_two.root.left.right = Node(7)
        self.assertRaises(MyException, tree_intersection, tree_one, tree_two)