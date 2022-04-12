from trees.trees import Node, BinaryTree

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