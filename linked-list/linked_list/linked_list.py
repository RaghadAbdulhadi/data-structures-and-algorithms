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

    def insert(self, value):
        """
        A function that adds a new node with the value to the the begining of the list, with O(1) time performance.
            Arguments: value
            Returns: Nothing
        """
        node = Node(value, self.head)
        self.head = node

    def insert_at_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            else: current.next = Node(value, None)

    def insert_values(self, values_list):
        for value in values_list:
            self.insert_at_end(value)

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        elif index == 0:
            self.head = self.head.next
            return
        
        # What will be changes is the pointer or the next of the previous node
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

        # What will be changes is the pointer or the next of the previous node
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

    ll = linked_list()
    ll2 = linked_list()

    ll.insert("Raghad")
    ll.insert("Gheed")
    ll.insert_at_end("Jood")
    ll.insert_values(["Omar", "Ayman", "Rajaa"])
    ll.remove_at(1)
    ll.remove_at(20)
    ll.insert_at()
    ll.insert_at(2,"Jood")
    ll.insert_at(0,"mugh")

    ll2.insert_values(["sewar", "rand", "raghad"])

    print(ll.includes("Rand"))
    print(ll.to_string())
    print(ll.get_length())

    print(ll2.to_string())