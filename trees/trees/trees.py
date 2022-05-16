# from trees.queue import Queue

import os


class Node:
    """
    A class that represents individual nodes in a tree
    """
    def __init__(self, value, left = None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root = None):
        """
        Intialize an object with an root node that currently does not have left and right nodes
        variable = BinaryTree(Node())
        """
        self.root = root

    def __str__(self):
        """
        String representation of the root node in a tree
        """
        return self.root.value

    def in_order_traversal(self): 
        """
        Left -> Root -> Right
            Arguments: None
            Return: array of the values, ordered appropriately
        """
        def walk(node):
            if node.left:
                walk(node.left)
            print(node.value, end=" ")
            if node.right:
                walk(node.right)
        walk(self.root) 


    def descending_traversal(self):
        def walk(node):
            if node.right:
                walk(node.right)
            print(node.value, end=" ")
            if node.left:
                walk(node.left)

        walk(self.root) 


    def pre_order_traversal(self): 
        """
        Root -> Left -> Right
            Arguments: None
            Return: Prints the values ordered appropriately
        ## Approach:
        - Root will be looked first and added to the stack
        - Start reading our function from the top, so root.value will be printed 
        - Check if the root has left node
        - If it has a left node, the left node will be send to the function recursively
        - The left node will be the new root, and added to the stack
        - Again the process will repeat until we reach the leaf node
        - The function will look for both left and right nodes they will be none so it will end execution of that method call
        - The leaf node will be popped from the stack and root will be reassigned to the previous node
        - Now it will look for the right node and repeat the whole process
        """
        nodes_list = []
        def walk(node):
            nonlocal nodes_list
            nodes_list.append(node.value)
            if node.left:
                walk(node.left)
            if node.right:
                walk(node.right)
        walk(self.root) 
        return nodes_list


    def post_order_traversal(self): 
        """
        Left -> Right -> Root
            Arguments: None
            Return: array of the values, ordered appropriately
        """
        def walk(node):
            if node.left:
                walk(node.left)
            if node.right:
                walk(node.right)
            print(node.value, end=" ")
        walk(self.root) 
    
    # Max Element Challenge
    ## Max Element Approach 1 ##
    def max_element_one(self):
        """
        A method that finds the maximum element stored in the tree and returns its value
        Arguments: none
        Returns: number
        """
        def find_max(node):
            if node == None:
                return float("-inf")
            left_node = find_max(node.left)
            print("leftnode: ", left_node)
            right_node = find_max(node.right)
            print("rightnode: ", right_node)
            return max(max(left_node, right_node), node.value)
        return find_max(self.root)    

    ## Max Element Approach 2 ##
    def max_element(self):
        """
        A method that finds the maximum element stored in the tree and returns its value
        Arguments: none
        Returns: number
        """
        max_element = 0
        def next_node(node):
            nonlocal max_element
            if node == None:
                return "Tree has no nodes"
            else:
                if max_element < int(node.value): 
                    max_element = int(node.value)
                    print("Max Element:", max_element)
                if node.left:
                    print("left side",node.left.value)
                    next_node(node.left)
                if node.right:
                    print("right side", node.right.value)
                    next_node(node.right)
        next_node(self.root)
        return max_element


class BST(BinaryTree):
    """
    A binary search tree is a type of tree in which nodes are organized in a manner where all values that are smaller than the root are placed to the left, and values that are greater than the root are placed to the right

    """

    def insert_node(self, node, value):
        # If the value is greater than the root then go the right side
        if value > node.value:
            if not node.right:
                node.right = Node(value)
                return
            self.insert_node(node.right, value)
        else:
        # If the value is smaller than the root then go the left side
            if not node.left:
                node.left = Node(value)
                return
            self.insert_node(node.left, value)
    

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            self.insert_node(self.root, value)


# Sum of odd values in a BinarySearchTree
    def check_odd_nodes(self):
        sum_node = 0
        if self.root.value % 2 != 0:
            sum_node += self.root.value
        def walk(node):
            nonlocal sum_node
            if node.left:
                if node.left.value % 2 != 0:
                    sum_node += node.left.value
                walk(node.left)
            if node.right:
                if node.right.value % 2 != 0:
                    sum_node += node.right.value
                walk(node.right)
        walk(self.root) 
        return sum_node


    def contains_node(self, node, value):
        if node == None:
            return False
        if value == node.value:
            return True
        if value > node.value:
            return self.contains_node(node.right, value)
        else:
            return self.contains_node(node.left, value)
        
    def contains(self, value):
        if not self.root:
            return None
        return self.contains_node(self.root, value)

    def delete(self, value):
        pass


# Breadth First Challenge
def breadth_first(tree):
    """
    A function that iterates through the tree by going through each level of the tree node-by-node using a queue.
        Arguments: tree
        Return: list of all values in the tree, in the order they were encountered
    """
    str_tree = []
    breadth_queue = Queue()
    breadth_queue.enqueue(tree.root)
    if tree.root == None:
        return "Tree is empty"

    while not breadth_queue.is_empty():
        node = breadth_queue.dequeue()
        if node:
            str_tree.append(node.value)
        if node.left:
            breadth_queue.enqueue(node.left)
        if node.right:
            breadth_queue.enqueue(node.right)
    return str_tree


# FizzBuzz Challenge
class MyException(Exception):
    pass

def tree_fizz_buzz(k_ary_tree):
    """
    A function that takes a k_ary_tree as an argument and returns a new k_ary_tree with the same structure as the original, but the values modified as follows:
    - If the value is divisible by 3, replace the value with “Fizz”
    - If the value is divisible by 5, replace the value with “Buzz”
    - If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
    - If the value is not divisible by 3 or 5, simply turn the number into a String
        Arguments: k_ary_tree
        Returns: new k_ary_tree
    """
    fizz_tree = BinaryTree()
    fizz_tree.root = k_ary_tree.root
    # nodes_list = []
    # print(fizz_tree.root.value)
    def walk(node):
        if fizz_tree.root == None:
            raise MyException("Binary Tree is empty")

        if int(node.value) % 5 == 0 and int(node.value) % 3 == 0:
            # nodes_list.append("FizzBuzz")
            node.value = "FizzBuzz"
            return

        elif int(node.value) % 3 == 0:
            # nodes_list.append("Fizz")
            node.value = "Fizz"

        elif int(node.value) % 5 == 0:
            # nodes_list.append("Buzz")
            node.value = "Buzz"

        elif int(node.value) % 5 != 0 and int(node.value) % 3 != 0:
            # nodes_list.append(str(node.value))
            node.value = str(node.value)

        if node.left:
            walk(node.left)

        if node.right:
            walk(node.right)
        

    walk(fizz_tree.root)
    return fizz_tree.pre_order_traversal()

# Check files in two different directories if they are equal in number
# def check_files(folder_one, folder_two):
#     sum_files_folder_one = 0
#     sum_files_folder_two = 0

#     if folder_one.root.value != None and folder_two.root.value != None:
#         def walk_one(node):
#             nonlocal sum_files_folder_one
#             if node.left:
#                 if (node.left.value).find(".") != -1:
#                     sum_files_folder_one += 1
#                 walk_one(node.left)
#             if node.right:
#                 if (node.right.value).find(".") != - 1:
#                     sum_files_folder_one += 1
#                 walk_one(node.right)
#         walk_one(folder_one.root)
#         print(sum_files_folder_one)
#         def walk_two(node):
#             nonlocal sum_files_folder_two
#             if node.left:
#                 if (node.left.value).find(".") != -1:
#                     sum_files_folder_two += 1
#                 walk_two(node.left)
#             if node.right:
#                 if (node.right.value).find(".") != -1:
#                     sum_files_folder_two += 1
#                 walk_two(node.right)
#         walk_two(folder_two.root)
#         print(sum_files_folder_two)

#         if sum_files_folder_two != sum_files_folder_one:
#             return False
#         return True
#     return False

# def check_files(folder_one, folder_two):
#     sum_files_folder_one = 0
#     sum_files_folder_two = 0

#     if folder_one.root.value != None and folder_two.root.value != None:
#         def walk_one(node):
#             nonlocal sum_files_folder_one
#             if node.left:
#                 if os.path.isfile(str(node.left.value)):
#                     sum_files_folder_one += 1
#                 walk_one(node.left)
#             if node.right:
#                 if os.path.isfile(str(node.right.value)):
#                     sum_files_folder_one += 1
#                 walk_one(node.right)
#         walk_one(folder_one.root)
#         print(sum_files_folder_one)
#         # def walk_two(node):
#         #     nonlocal sum_files_folder_two
#         #     if node.left:
#         #         if os.path.isfile(str(node.left.value)):
#         #             sum_files_folder_two += 1
#         #         walk_two(node.left)
#         #     if node.right:
#         #         if os.path.isfile(str(node.right.value)):
#         #             sum_files_folder_two += 1
#         #         walk_two(node.right)
#         # walk_two(folder_two.root)
#         # print(sum_files_folder_two)

#         if sum_files_folder_two != sum_files_folder_one:
#             return False
#         return True
#     return False
  


# def check_files(folder_one, folder_two):
#     sum_files_folder_one = 0
#     sum_files_folder_two = 0

#     if folder_one.root.value != None and folder_two.root.value != None:
#         def walk_one(node):
#             nonlocal sum_files_folder_one
#             if node.left:
#                 if os.path.isfile(str(node.left.value)):
#                     sum_files_folder_one += 1
#                 walk_one(node.left)
#             if node.right:
#                 if os.path.isfile(str(node.right.value)):
#                     sum_files_folder_one += 1
#                 walk_one(node.right)
#         walk_one(folder_one.root)
#         print(sum_files_folder_one)

def check_files(folder_one, folder_two):
    sum_files_folder_one = 0
    sum_files_folder_two = 0

    if folder_one.root.value != None and folder_two.root.value != None:
        def walk_one(node, folder_num):
            nonlocal sum_files_folder_one
            nonlocal sum_files_folder_two
            if os.path.isfile(str(node.value)):
                if folder_num == 2:     
                    sum_files_folder_two += 1
                if folder_num == 1:
                    sum_files_folder_one += 1 
            if node.left:
                walk_one(node.left, folder_num)
            if node.right:
                walk_one(node.right, folder_num)
        walk_one(folder_two.root, 2)
        walk_one(folder_one.root,1)
        if sum_files_folder_two != sum_files_folder_one:
            return False
        return True
    return False



if __name__ == "__main__":
    from queue import Queue
    folder_one = BinaryTree(Node("/home/raghad/Code Challenges/"))
    folder_one.root.left = Node("/home/raghad/Code Challenges/data-structures-and-algorithms/")
    folder_one.root.right = Node("/home/raghad/Code Challenges/data-structures-and-algorithms/stack_and_queue/stack_and_queue/pseudo_queue.py")
    folder_one.root.left.left = Node("/home/raghad/Code Challenges/data-structures-and-algorithms/stack_and_queue/stack_and_queue/pseudo_queue.py")
    folder_one.root.left.right = Node("/home/raghad/Code Challenges/data-structures-and-algorithms/stack_and_queue/stack_and_queue/pseudo_queue.py")

    folder_two = BinaryTree(Node("/home/raghad/Code Challenges/"))
    folder_two.root.left = Node("/home/raghad/Code Challenges/data-structures-and-algorithms/")
    folder_two.root.right = Node("/home/raghad/Code Challenges/data-structures-and-algorithms/stack_and_queue/stack_and_queue/pseudo_queue.py")
    folder_two.root.left.left = Node("/home/raghad/Code Challenges/data-structures-and-algorithms/stack_and_queue/stack_and_queue/pseudo_queue.py")
    folder_two.root.left.right = Node("/home/raghad/Code Challenges/data-structures-and-algorithms/stack_and_queue/stack_and_queue/pseudo_queue.py")
    print(check_files(folder_one,folder_two))

    # binary_search_tree = BST()
    # binary_search_tree.insert(3)
    # binary_search_tree.insert(5)
    # binary_search_tree.insert(7)
    # binary_search_tree.insert(2)
    # binary_search_tree.insert(15)
    # binary_search_tree.insert(5)
    # print(binary_search_tree.in_order_traversal())
    # print(binary_search_tree.check_odd_nodes())
    # print(binary_search_tree.sum_odd_nums())
    # tree = BinaryTree(Node(25))
    # tree.root.left = Node(1)
    # tree.root.right = Node("1")
    # tree.root.right.right = Node(15)
    # tree.root.left.right = Node(5)
    # tree.root.left.left = Node(3)
    # tree.root.right.left = Node(8)
    # print(breadth_first(tree))
    # print(tree.root.right.value)
    # print("Final Max Element:", tree.max_element())
    # print(tree.pre_order_traversal())
    # print(tree_fizz_buzz(tree))
#       4
#   1      12
# 0   2  8    16

# def find_node(node, value):
#     if node == None:
#         return 

# def delete(self, value):
#     if node 
        
    


# 12 => 8 will be in place of 12
# 1 => 2 will be in place of 1
# 4 => 2 will be in place of 4
# if leaf node => delete it 

# if node.left: 
#   walk(node.left)
# print(node.value)  
# if node.right:
#   walk(node.right)
#   
#
# 1, 2,3,4, 4.5,5,6
# Add node(root) to the queue
# print
# Add its children left then right to a queue
  
  # print(tree)
  # print(tree.root.left.value)
  # print(tree.root.right.value)

# tree.pre_order_traversal()
# print()
# tree.in_order_traversal()
# print()
# tree.post_order_traversal()
# print()
# tree.descending_traversal()
# right , root , left 
# tree.bfs_traversal()


#    100 
# 50     102
#     101    104
#               150
  
# binary_search_tree.insert("10")
# binary_search_tree.in_order_traversal()  
# print(binary_search_tree.root.value) # 100
# print(binary_search_tree.root.left.value) # 50
# print(binary_search_tree.root.right.value) # 102
# print(binary_search_tree.root.right.left.value) # 101
# print(binary_search_tree.root.right.right.value) # 104
# print(binary_search_tree.root.right.right.right.value) # 150

#   print(binary_search_tree.contains(104))


