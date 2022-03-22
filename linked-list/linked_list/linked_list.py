class Node:
    """
    A class that represents individual elements in a linked list
    """

    def __init__(self, value=None, next=None):
        #Value stored in the Node
        self.value = value
        #Pointer to the next Node
        self.next = next


class linked_list:
    """
    A class that instantiate, insert at the begining, insert at the end, removes nodes from a linked list and get the length of the list and checks if it contains a specific value.
    """

    def __init__(self):
        """
        When instantiation an empty linked list will be created.
        """
        #Points to the head of the linked list
        self.head = None

    def insert_at_beginning(self, value):
        """
        A function that adds a new node with the value to the the begining of the list, with O(1) time performance.
            Arguments: value
            Returns: The linked list with the new node added at the begining of the list
        """
        node = Node(value, self.head)
        self.head = node

    def append(self, value):
        """
        A function that adds a new node with the value to the the end of the list.
            Arguments: value
            Returns: The linked list with the new node at the end of the linked list
        """
        if self.head is None:
            self.head = Node(value, None)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            else: current.next = Node(value, None)

    def insert_after(self, value, new_value):
        """
        A function that adds a new node with the value after the given value of the node in the list.
            Arguments: value, new_value
            Returns: The linked list with the new node added after the given value of existing node
        """
        if self.head is None:
            self.head = Node(new_value, None)
        else:
            current = self.head
            while current:
                if current.value == value:
                    node = Node(new_value, current.next)
                    current.next = node
                    break
                current = current.next

    def insert_before(self, value, new_value):
        """
        A function that adds a new node with the value before the given value of the node in the list.
            Arguments: value, new_value
            Returns: The linked list with the new node added before the given value of existing node
        """
        if self.head is None:
            self.head = Node(new_value, None)
        else:
            current = self.head
            while current:
                if current.next.value == value:
                    node = Node(new_value, current.next)
                    current.next = node
                    break
                current = current.next

    def kth_from_end(self, k):
        """
        A function that returns the value of the node at the k position from the tail of the linked list.
        Arguments: Number (k)
        Returns: node’s value that is k places from the tail of the linked list
        """
        if k < 0 or k >= self.get_length():
            # raise Exception("Invalid Index")
            return "Invalid Index"
        else:
            count = self.get_length() -1
            current = self.head
            while current:
                if k == count:
                    return current.value
                current = current.next
                count = count - 1


    def insert_values(self, values_list):
        for value in values_list:
            self.append(value)

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def remove_at(self, index):
        """
        A function that removes node with a specific index(first, second, third node) from the list
        Input: index of the node
        Output: L.L with the node removed
        """
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        elif index == 0:
            self.head = self.head.next
            return
        
        # What will be changed is the pointer or the next of the previous node
        count = 0
        current = self.head
        while current:
            if count == index -1:
                current.next = current.next.next
                break
            current = current.next
            count += 1

    def insert_at(self, index, value):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
            
        elif index == 0:
            self.insert(value)
            return

        # What will be changed is the pointer or the next of the previous node
        count = 0
        current = self.head
        while current:
            if count == index -1:
                node = Node(value, current.next)
                current.next = node
                break
            current = current.next
            count += 1

    def includes(self, value):
        """
        A function that indicates whether the value exists as a Node's value.
            Arguments: value
            Returns: Boolean
        """
        if self.head == None:
            return False
        else:
            current = self.head
            while current is not None:
                if current.value == value:
                    return True
                current = current.next
            return False

    def remove_all_nodes(self):
        while self.head != None:
            current = self.head
            self.head = self.head.next
            current = None



    def zip_lists(self, linked_list_one, linked_list_two):
        """
        A function that zips two linked lists together into one so that the nodes alternate between the two lists, with space equal to O(1)
            Arguments: two linked lists
            Return: a reference to the the zipped list.
        """
        current_one = linked_list_one.head
        current_two = linked_list_two.head
        while current_one is not None and current_two is not None:
            linked_list_one.insert_after(current_one.value,current_two.value)
            current_one = current_one.next.next
            current_two = current_two.next
        if current_one == None and current_two != None:
            linked_list_one.append(current_two.value)
        linked_list_two.remove_all_nodes()
        return linked_list_one
    
    
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
        

if __name__ == '__main__':


    linked_list_one = linked_list()
    linked_list_two = linked_list()
    linked_list_one.insert_values([1,3,2])
    linked_list_two.insert_values([5,9,4])
    linked_list_two.zip_lists(linked_list_one, linked_list_two)
    print(linked_list_one.to_string())

    linked_list_one = linked_list()
    linked_list_two = linked_list()
    linked_list_one.insert_values([1,3])
    linked_list_two.insert_values([5,9,4])
    linked_list_one.zip_lists(linked_list_one, linked_list_two)
    print(linked_list_one.to_string())

    linked_list_one = linked_list()
    linked_list_two = linked_list()
    linked_list_one.insert_values([1,3,2])
    linked_list_two.insert_values([5,9])
    linked_list_two.zip_lists(linked_list_one, linked_list_two)
    print(linked_list_one.to_string())
    print(linked_list_two.to_string())



    # ll = linked_list()
    # ll2 = linked_list()
    # ll.insert_at_beginning("Raghad")
    # ll.insert_at_beginning("Gheed")
    # ll.append("Jood")
    # ll.insert_after("Raghad", "Omar")
    # ll.insert_before("Raghad", "mugh")
    # ll.insert_before("Gheed", "moayad")
    # ll.insert_values(["Omar", "Ayman", "Rajaa"])
    # ll.remove_at(1)
    # ll.remove_at(20)
    # ll.insert_at()
    # ll.insert_at(2,"Jood")
    # ll.insert_at(0,"mugh")
    # ll2.insert_values(["sewar", "rand", "raghad"])
    # print(ll.kth_from_end(0))
    # print(ll.kth_from_end(2))
    # print(ll.kth_from_end(4))
    # print(ll.includes("Rand"))
    # print(ll.to_string())
    # print(ll.get_length())
    # print(ll2.to_string())