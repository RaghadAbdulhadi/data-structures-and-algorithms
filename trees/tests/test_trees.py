from trees.trees import TNode, BinaryTree, BinarySearchTree
import pytest

def test_contains_value():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.add(4)
    binary_search_tree.add(2)
    binary_search_tree.add(8)
    binary_search_tree.add(5)
    binary_search_tree.add(10)
    actual = binary_search_tree.contains(4)
    expected = True
    assert actual == expected

def test_doesnt_contains_value():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.add(4)
    binary_search_tree.add(2)
    binary_search_tree.add(8)
    binary_search_tree.add(5)
    binary_search_tree.add(10)
    actual = binary_search_tree.contains(11)
    expected = False
    assert actual == expected

def test_instantiate_empty_tree():
    binary_search_tree = BinarySearchTree()
    actual = binary_search_tree.root
    expected = None
    assert actual == expected

def test_insert_nodes_to_tree_root():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.add(4)
    binary_search_tree.add(2)
    binary_search_tree.add(8)
    binary_search_tree.add(5)
    binary_search_tree.add(10)
    actual = binary_search_tree.root.value
    expected = 4
    assert actual == expected

def test_insert_nodes_to_tree_left():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.add(4)
    binary_search_tree.add(2)
    binary_search_tree.add(8)
    binary_search_tree.add(5)
    binary_search_tree.add(10)
    actual = binary_search_tree.root.left.value
    expected = 2
    assert actual == expected
    
def test_insert_nodes_to_tree_right():
    binary_search_tree = BinarySearchTree()
    binary_search_tree.add(4)
    binary_search_tree.add(2)
    binary_search_tree.add(8)
    binary_search_tree.add(5)
    binary_search_tree.add(10)
    actual = binary_search_tree.root.right.value
    expected = 8
    assert actual == expected

def test_preorder(test_tree):
    actual = test_tree.traversal_type("preorder")
    expected = [1, 2, 4, 5, 3, 6, 7, 8]
    assert actual == expected

def test_inorder(test_tree):
    actual =test_tree.traversal_type("inorder")
    expected = [4, 2, 5, 1, 6, 3, 7, 8]
    assert actual == expected

def test_postorder(test_tree):
    
    actual = test_tree.traversal_type("postorder")
    expected = [4, 2, 5, 6, 3, 7, 8, 1]
    assert actual == expected

@pytest.fixture
def test_tree():
    # Nodes
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node5 = TNode(5)
    node6 = TNode(6)
    node7 = TNode(7)
    node8 = TNode(8)

    # Binary Tree
    tree = BinaryTree()
    tree.root = node1
    tree.root.left = node2
    tree.root.right = node3
    tree.root.left.left = node4
    tree.root.left.right = node5
    tree.root.left.right = node5
    tree.root.right.left = node6
    tree.root.right.right = node7
    tree.root.right.right.right = node8
    return tree













## Can successfully instantiate an empty tree
## Can successfully instantiate a tree with a single root node
## For a Binary Search Tree, can successfully add a left child and right child properly to a node
# Can successfully return a collection from a preorder traversal
# Can successfully return a collection from an inorder traversal
# Can successfully return a collection from a postorder traversal
## Contains -> True or False