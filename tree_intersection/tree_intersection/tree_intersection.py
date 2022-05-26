# from trees import BinaryTree, Node
# from hashtable import Hashtable

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
        if len(hash_table.table[hashed_key]) % 2 == 0:
            values_set.add(hash_table.table[hashed_key][len(hash_table.table[hashed_key]) - 1][0])
            values_set.add(hash_table.table[hashed_key][len(hash_table.table[hashed_key]) - 2][0])
        # print(hash_table.table)
    walk(tree_one.root, 1)
    walk(tree_two.root, 2)
    if len(values_set) == 0:
        raise MyException("No common values")
    return values_set

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

class MyException(Exception):
    pass
class Hashtable:
    def __init__(self, size= 100):
        # initialize the size of the list
        self.size = size
        self.table = [None]*size

    def hash(self, key):
        """
        A method that takes in a key and returns the index of the key in the collection of that key
            Arguments: key
            Returns: Index in the collection for that key
        """
        sum_of_ascii = 0
        for charc in key:
            charc_ascii = ord(charc)
            sum_of_ascii += charc_ascii
        hashed_key = (sum_of_ascii) % self.size

        return hashed_key

    def set(self, key, value):
    # def __setitem__(self, key, value):
        """
        A method that takes in a key and a value, it hashes the key, and sets the key and value pair in the table, handles collisions as needed.
            Arguments: key, value
            Returns: Nothing
        """
        # get the hashed key from the hash method
        hashed_key = self.hash(key)
        # check if the bucket is empty at the hashed_key index, add the key/value pair
        if not self.table[hashed_key]:
            self.table[hashed_key] = [[key, value]]
        # if the bucket is not empty, append the key/value pair
        else:
            self.table[hashed_key].append([key, value])

    def get(self, key):
    # def __getitem__(self, key):
        """
        A method that returns the value associated with a specific key that is passed to the method as an argument.
            Arguments: key
            Returns: Value associated with that key in the table
        """
        # call the get hash method and send the key to it
        hashed_key = self.hash(key)
        # lookup the index of the value from the table
        # return the value stored in that index
        return self.table[hashed_key][0][1]

    def __delitem__(self, key):
        """                
        A method that deleted an key and value from the table
            Arguments: key
            Returns: Nothing
        """
        # call the get hash method and send the key to it
        hashed_key = self.hash(key)
        # Set this particular key's value to be none
        self.table[hashed_key] = None


    def contains(self, key):
        """
        A method that takes in a key and checks if it is in the table or not.
            Arguments: key
            Returns: Boolean, indicating if the key exists in the table already.
        """
        hashed_key = self.hash(key)
        if self.table[hashed_key] == None:
            return False
        return True
        
    def keys(self):
        """
        A method that returns a collection of keys
            Arguments: None
            Returns: Collection of keys
        """
        keys_collection = []
        for idx, value in enumerate(self.table):
            if self.table[idx] != None:
                if len(self.table[idx]) == 1:
                    keys_collection.append(self.table[idx][0][0])
                else:
                    keys_collection.append(self.table[idx][0][0])
                    keys_collection.append(self.table[idx][1][0])  
        return keys_collection
if __name__ == "__main__":
    from trees import BinaryTree, Node
    from hashtable import Hashtable
    # Tree One
    tree_one = BinaryTree(Node(1))
    tree_one.root.left = Node(20)
    tree_one.root.left.left = Node(3)
    tree_one.root.left.right = Node(44)
    tree_one.root.left.left.left = Node(55)
    tree_one.root.left.left.right = Node(46)
    tree_one.root.left.right.left = Node(170)
    # tree_one.root.left.right.right = Node(88)
    # tree_one.root.right = Node(2)
    # tree_one.root.right.left = Node(20)
    # tree_one.root.right.right = Node(3)
    # tree_one.root.right.right.right = Node(5)
    # tree_one.root.right.right.left = Node(60)
    # tree_one.root.right.left.left = Node(8)
    # tree_one.root.right.left.right = Node(7)
    # Tree Two
    tree_two = BinaryTree(Node(1))
    tree_two.root.left = Node(20)
    tree_two.root.left.left = Node(3)
    tree_two.root.left.right = Node(44)
    tree_two.root.left.left.left = Node(55)
    tree_two.root.left.left.right = Node(46)
    tree_two.root.left.right.left = Node(170)
    # tree_two.root.left.right.right = Node(88)
    # tree_two.root.right = Node(2)
    # tree_two.root.right.left = Node(20)
    # tree_two.root.right.right = Node(3)
    # tree_two.root.right.right.right = Node(5)
    # tree_two.root.right.right.left = Node(60)
    # tree_two.root.right.left.left = Node(8)
    # tree_two.root.right.left.right = Node(7)

    print(tree_intersection(tree_one, tree_two))
