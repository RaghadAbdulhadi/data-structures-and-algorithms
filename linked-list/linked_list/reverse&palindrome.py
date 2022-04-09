class Node:
    """
    A class that represents individual elements in a linked list
    """

    def __init__(self, value=None, next=None, previous=None):
        #Value stored in the Node
        self.value = value
        #Pointer to the next Node
        self.next = next
        #Pointer to the previous Node
        self.previous = previous


class linked_list:
    """
    A class that instantiate, 
    """

    def __init__(self):
        """
        When instantiation an empty linked list will be created.
        """
        #Points to the head of the linked list
        self.head = None

    def append(self, value):
        """
        A function that adds a new node with the value to the the end of the list.
            Arguments: value
            Returns: The linked list with the new node at the end of the linked list
        """
        if self.head is None:
            node = Node(value)
            node.previous = None
            self.head = node
        else:
            node = Node(value)
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.previous = current
            node.next = None

    def insert_at_beginning(self, value):
        if self.head == None:
            node = Node(value)
            self.head = node
        else:
            node = Node(value)
            current = self.head
            current.previous = node
            self.head = node
            self.head.next = current
            self.head.previous = None


            
    #         # self.head.previous = node
    #         # node.next = self.head
    #         # self.head = node
    #         # node.previous = None
    
    def reverse_linked_list(self, linkedlist):
        if self.head is None:
            return "Linked list is empty"
        else:
            previous = None
            current = linkedlist.head
            next = None
            while current:
                next = current.next
                current.next = previous
                previous = current
                current = next
            linkedlist.head = previous
            return linkedlist

    #                     ## TRACE ##
    #         # { 0 } -> { 1 } -> { 2 } -> { 3 } -> None

    #         # // previous = None
    #         # // current = linkedlist.head
    #         # // next = None

    #         # // current = 0 --> True
    #         #     // next = current.next --> 1
    #         #     // current.next = previous --> None
    #         #     // previous = current --> 0
    #         #     // current = next --> 1
    #         # // current = 1 --> True
    #         #     // next = current.next --> 2
    #         #     // current.next = previous --> 0
    #         #     // previous = current --> 1
    #         #     // current = next --> 2
    #         # // current = 2 --> True
    #         #     // next = current.next --> 3
    #         #     // current.next = previous --> 1
    #         #     // previous = current --> 2
    #         #     // current = next --> 3
    #         # // current = 3 --> True
    #         #     // next = current.next --> None
    #         #     // current.next = previous --> 2
    #         #     // previous = current --> 3
    #         #     // current = next --> None

    #         # // current = None --> False
    #         #     // Exit the loop
    #         # // linkedlist.head = previous
    #         # //return { 3 } -> { 2 } -> { 1 } -> { 0 } -> None

    def is_palindrome(self, linkedlist):
        current_linked_list = linkedlist
        current_before = current_linked_list.head
        linkedlist_reversed = linkedlist.reverse_linked_list(linkedlist)
        current_after = linkedlist_reversed.head
        while  current_before and current_after:
            if current_before.value != current_after.value:
                return False
            else:
                current_before = current_before.next
                current_after = current_after.next
        return True


        """
        1. loop over both the original linked list and the reversed linked list
        2. Check if each value in the original list is equal to the value in the reversed list
        3. If they are all equal --> return True
        4. Else return False
        """




        # while current_before and current_after:
        #     if current_before.value != current_after.value:
        #         return False
        #     else:
        #         current_before = current_before.next
        #         current_after = current_after.next
        #     return True
            
    def to_string(self):
        """
        A function that takes no arguments and returns a formatted string.
            Arguments: none
            Returns: String representation of the values in the linked list.
                    "{ a } -> { b } -> { c } -> None"
        """
        linked_list_str = ""
        if self.head is None:
            linked_list_str = "Linked list is empty"
        else:
            current = self.head
            while current:
                linked_list_str += "{ " + str(current.value) + " }" + ' -> '
                current = current.next
            linked_list_str += "None"
        return linked_list_str



if __name__ == "__main__":
    linkedlist = linked_list()
    linkedlist.insert_at_beginning("t")
    linkedlist.insert_at_beginning("b")
    linkedlist.insert_at_beginning("c")
    linkedlist.insert_at_beginning("o")
    linkedlist.insert_at_beginning("c")
    linkedlist.insert_at_beginning("a")
    linkedlist.insert_at_beginning("t")


    # linkedlist.append("R")

    #linkedlist.reverse_linked_list(linkedlist)
    print(linkedlist.is_palindrome(linkedlist))
    #print(linkedlist.to_string())




    