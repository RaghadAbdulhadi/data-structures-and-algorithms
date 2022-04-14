# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class Stack:
#     ## max_element = []
#     def __init__(self):
#         self.top = None
        

#     def push(self,value):
#         node = Node(value)
#         node.next = self.top
#         self.top = node
#         ## Stack.max_element.append(int(self.top.value))
    
#     def pop(self):
#         if self.top == None:
#             return "Queue is empty"
#         else:
#             temp = self.top
#             self.top = self.top.next
#             temp.next = None
#             return temp.value

#     def peek(self):
#         if self.top == None:
#             return "Stack is empty"
#         self.top.value
        
#     def is_empty(self):
#         if self.top == None:
#             return True
#         return False

#     ##Approach#1 O(n) Time Complexity##
#     def get_max(self):
#         """
#         A function that returns the maximum element in the Stack
#             Arguments: None
#             Return: Value of the maximum element
#         """
#         current = self.top
#         max_element = 0
#         while current:
#             if int(current.value) < int(max_element):
#                 current = current.next
#             elif int(current.value) > int(max_element):
#                 max_element = int(current.value)
#                 current = current.next  
#         return max_element

#     ##Approach#2##
#     @staticmethod
#     def get_max():
#         return max(Stack.max_element)
    
#     def to_string(self):
#         stack_str = ""
#         if self.top == None:
#             stack_str = "Stack is empty"
#         else:
#             current = self.top
#             while current:
#                 stack_str += "{ " + str(current.value) + " }" + " -> "
#                 current = current.next
#             stack_str += "None"
#         return stack_str


# if __name__ == "__main__":
#     stack = Stack()
#     stack.push("190")
#     stack.push("5")
#     stack.push("2")
#     stack.push("6")
#     stack.push("100")
#     stack.push("9")
#     stack.push("2")
#     stack.push("150")
#     stack.push("78")
#     stack.push("1")
#     stack.pop()
#     print(stack.get_max())
#     print(stack.to_string())

# # Approach#3
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        # Max of the max_element and the top of the max_stack
        value = max(value, self.max_stack[-1] if self.max_stack else value)
        self.max_stack.append(value)
    
    # def pop(self):
    #     self.stack.pop()
    #     self.max_stack.pop()

    # def peek(self):
    #     return self.stack[-1]

    def get_max(self):
        return self.max_stack[-1]

if __name__ == '__main__':
    max_stack = MaxStack()
    max_stack.push(-610)
    max_stack.push(55)
    max_stack.push(15)
    max_stack.push(50)
    max_stack.push(5)
    max_stack.push(477)
    max_stack.push(5)
    print(max_stack.get_max())