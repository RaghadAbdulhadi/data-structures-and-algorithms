class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        # A value for the root will be passed to the tree
        self.root = None
    def traversal_type(self, traversal_type):
        if traversal_type == "preorder":
            return self.pre_order(self.root, [])
        elif traversal_type == "inorder":
            return self.in_order(self.root, [])
        elif traversal_type == "postorder":
            return self.post_order(self.root, [])

    def pre_order(self, node, nodes_list = []):
        """
        Root -> Left -> Right
        Arguments: None
        Return: list of the values, ordered appropriately
        """
        if node:
            nodes_list.append(node.value)
            nodes_list = self.pre_order(node.left, nodes_list)
            nodes_list = self.pre_order(node.right, nodes_list)
        return nodes_list

    def in_order(self, node, nodes_list = []):
        """
        Left -> Root -> Right
        Arguments: None
        Return: array of the values, ordered appropriately
        """
        if node:
            nodes_list = self.in_order(node.left, nodes_list)
            nodes_list.append(node.value)
            nodes_list = self.in_order(node.right, nodes_list)
        return nodes_list

    def post_order(self, node, nodes_list = []):
        """
        Left -> Right -> Root
        Arguments: None
        Return: array of the values, ordered appropriately
        """
        if node:
            nodes_list = self.in_order(node.left, nodes_list)
            nodes_list = self.in_order(node.right, nodes_list)
            nodes_list.append(node.value)
        return nodes_list

class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
        A method that adds a new node with that value in the correct location in the binary search tree.
            Arguments: value
            Return: nothing
        """
        if self.root == None:
            self.root = TNode(value)
        else:
            self._add(value, self.root)
    def _add(self, value, current_node):
        if value < current_node.value:
            if current_node.left == None:
                current_node.left = TNode(value)
            else:
                self._add(value, current_node.left)
        elif value > current_node.value:
            if current_node.right == None:
                current_node.right = TNode(value)
            else:
                self._add(value, current_node.right)
        else:
            print("Value is already in the binary search tree")

    def contains(self, value):
        """
        A method that checks whether or not the value is in the tree at least once.
            Argument: value
            Return: boolean
        """
        if self.root:
            is_found = self._contains(value, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _contains(self, value, current_node):
        if value > current_node.value and value < current_node.right.value:
            return self._contains(value, current_node.right)
        elif value < current_node.value and current_node.left.value:
            return self._contains(value, current_node.left)
        elif value == current_node.value:
            return True

if __name__ == "__main__":
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

    print(tree.traversal_type("preorder"))
    print(tree.traversal_type("inorder"))
    print(tree.traversal_type("postorder"))

    # Binary Search Tree

    binary_search_tree = BinarySearchTree()
    binary_search_tree.add(4)
    binary_search_tree.add(2)
    binary_search_tree.add(8)
    binary_search_tree.add(5)
    binary_search_tree.add(10)

    # print(binary_search_tree.contains(20))
    # print(binary_search_tree.contains(4))
    print(binary_search_tree.contains(11))


#      1
#    /   \
#   2     3
#  / \   / \
# 4   5  6  7
#            \ 
#             8



