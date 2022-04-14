# from queue import Queue
# from trees.trees import Node, BinaryTree

# def breadth_first(tree):
#     """
#     A function that iterates through the tree by going through each level of the tree node-by-node using a queue.
#         Arguments: tree
#         Return: list of all values in the tree, in the order they were encountered
#     """
#     str_tree = []
#     breadth_queue = Queue()
#     breadth_queue.enqueue(tree.root)

#     while not breadth_queue.is_empty():
#         node = breadth_queue.dequeue()
#         if node:
#             str_tree.append(node.value)
#         if node.left:
#             breadth_queue.enqueue(node.left)
#         if node.right:
#             breadth_queue.enqueue(node.right)
#     return str_tree


# if __name__ == "__main__":
#     from queue import Queue
#     tree = BinaryTree(Node(4))
#     tree.root.left = Node(1)
#     tree.root.right = Node(12)
#     tree.root.right.right = Node(16)
#     tree.root.left.right = Node(2)
#     tree.root.left.left = Node(0)
#     tree.root.right.left = Node(8)
#     print(breadth_first(tree))