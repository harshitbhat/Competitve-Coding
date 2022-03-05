from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    # ---------------------------------------------------------------------------- #
    #                            Get Head of linked List                           #
    # ---------------------------------------------------------------------------- #
    def get_head(self):
        return self.head

    # ---------------------------------------------------------------------------- #
    #                            Check if list is empty                            #
    # ---------------------------------------------------------------------------- #
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # ---------------------------------------------------------------------------- #
    #                                Insert at head                                #
    # ---------------------------------------------------------------------------- #
    def insert_at_head(self, data):
        tempNode = Node(data)

        tempNode.next = self.head
        self.head = tempNode

        return self.head
    
    # ---------------------------------------------------------------------------- #
    #                               Insertion at Tail                              #
    # ---------------------------------------------------------------------------- #
    def insert_at_tail(self, data):
        tempNode = Node(data)

        if self.is_empty():
            self.head = tempNode
            return self.head
        
        temp = self.head

        while temp.next is not None:
            temp = temp.next
        
        temp.next = tempNode
        return self.head

    # ---------------------------------------------------------------------------- #
    #                            Search in a linked list                           #
    # ---------------------------------------------------------------------------- #
    def search(self, value):
        temp = self.head

        while temp:
            if temp.data is value:
                return True
            temp = temp.next
        
        return False

    # ---------------------------------------------------------------------------- #
    #                               Delete from Head                               #
    # ---------------------------------------------------------------------------- #
    def delete_at_head(self):
        if self.is_empty():
            return
        
        self.head = self.head.next
        return self.head

    # ---------------------------------------------------------------------------- #
    #                               Seletion by value                              #
    # ---------------------------------------------------------------------------- #
    def delete(self, value):
        if self.is_empty():
            return False
        
        if self.head.data == value:
            self.head = self.head.next
            return True
        
        temp = self.head

        while temp and temp.next:
            if temp.next.data == value:
                temp.next = temp.next.next
                return True
            temp = temp.next
        
        return False


    # ---------------------------------------------------------------------------- #
    #                         Complementary Print function                         #
    # ---------------------------------------------------------------------------- #
    def print_list(self):
        if self.is_empty():
            print("The list is empty")
            return
        
        temp = self.head

        while temp.next is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(temp.data)

# ------------------------- End of Linked List Class ------------------------- #


# ---------------------------------------------------------------------------- #
#                                Main execution                                #
# ---------------------------------------------------------------------------- #

# lst = LinkedList()  # Linked List created
# print("Head: ", lst.get_head())  # Returns None since headNode does not contain any data
# print("Is Empty: ", lst.is_empty())  # Returns true

list = LinkedList()
list.print_list()

n = 5

print("Inserting values in the list")
for i in range(5):
    list.insert_at_head(n-i)

list.print_list()

print("Insert at tail")
list.insert_at_tail(100)
list.print_list()

print("Deletion")
list.delete_at_head()
list.print_list()

print("Delete value")
list.delete(2)
list.print_list()