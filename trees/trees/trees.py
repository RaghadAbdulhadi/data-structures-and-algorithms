from trees.queue import Queue

class Node:
    def __init__(self, value, left = None,right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def __str__(self):
        return self.root.value

    def in_order_traversal(self): 
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
        def walk(node):
            print(node.value, end=" ")
            if node.left:
                walk(node.left)
            if node.right:
                walk(node.right)
        walk(self.root) 


    def post_order_traversal(self): 
        def walk(node):
            if node.left:
                walk(node.left)
            if node.right:
                walk(node.right)
            print(node.value, end=" ")
        walk(self.root) 
    
            ## Approach 1 ##
    # def max_element(self):
    #     """
    #     A method that finds the maximum element stored in the tree and returns its value
    #     Arguments: none
    #     Returns: number
    #     """
        # def find_max(node):
        #     if node == None:
        #         return float("-inf")
        #     left_node = find_max(node.left)
        #     print("leftnode: ", left_node)
        #     right_node = find_max(node.right)
        #     print("rightnode: ", right_node)
        #     return max(max(left_node, right_node), node.value)
        # return find_max(self.root)    

            ## Approach 2 ##
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

    def insert_node(self, node, value):
        if value > node.value:
            if not node.right:
                node.right = Node(value)
                return
            self.insert_node(node.right, value)
        else:
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
    
      
if __name__ == "__main__":
    from queue import Queue
    tree = BinaryTree(Node(4))
    tree.root.left = Node(1)
    tree.root.right = Node(12)
    tree.root.right.right = Node(16)
    tree.root.left.right = Node(2)
    tree.root.left.left = Node(0)
    tree.root.right.left = Node(8)
    print(breadth_first(tree))
    print(tree.root.right.value)
    print("Final Max Element:", tree.max_element())
    tree.in_order_traversal()
    tree.delete(12)
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

#   binary_search_tree = BST()
#   binary_search_tree.insert(100)
#   binary_search_tree.insert(102)
#   binary_search_tree.insert(104)
#   binary_search_tree.insert(101)
#   binary_search_tree.insert(150)
#   binary_search_tree.insert(50)

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


