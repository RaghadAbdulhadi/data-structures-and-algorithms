from trees.trees import Node, BinaryTree
from trees.breadth_first import breadth_first

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