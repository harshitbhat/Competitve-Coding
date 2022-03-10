import imp
from Node import Node

class LinkedList:
    def __init__(self):
        self.head_node = None
    
    def get_head(self):
        return self.head_node
    
    def is_empty(self):
        if self.is_empty() is None:
            return True
        return False
    
    def insert_at_head(self, data):
        temp_node = Node(data)

        if self.is_empty():
            self.head_node = temp_node
            return self.head_node
        
        temp_node.next_element = self.head_node
        self.head_node.previous_element = temp_node
        self.head_node = temp_node
        return self.head_node

    def delete(self, value):
        deleted = False
        if self.is_empty():
            print("List is Empty")
            return deleted

        current_node = self.get_head()

        if current_node.data is value:
            # Point head to the next element of the first element
            self.head_node = current_node.next_element
            if(current_node.next_element != None and current_node.next_element.previous_element != None):
                # Point the next element of the first element to None
                current_node.next_element.previous_element = None
                deleted = True  # Both links have been changed.
                print(str(current_node.data) + " Deleted!")

            return deleted

        # Traversing/Searching for node to Delete
        while current_node:
            if value is current_node.data:
                if current_node.next_element:
                    # Link the next node and the previous node to each other
                    prev_node = current_node.previous_element
                    next_node = current_node.next_element
                    prev_node.next_element = next_node
                    next_node.previous_element = prev_node
                    # previous node pointer was maintained in Singly Linked List

                else:
                    current_node.previous_element.next_element = None
                deleted = True
                break
            # previousNode = tempNode was used in Singly Linked List
            current_node = current_node.next_element

        if deleted is False:
            print(str(value) + " is not in the List!")
        else:
            print(str(value) + " Deleted!")
        return deleted


    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False

        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element

        print(temp.data, "-> None")
        return True

