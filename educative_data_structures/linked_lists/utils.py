class Node:
    """Class which defines a node with data and next"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        """Function to print the contents of the linked list: using next as a traversing parameter"""
        curr_node = self.head
        while curr_node:
            print(curr_node.data)

            curr_node = curr_node.next
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def prepend(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node(self,prev_node, data):
        if not prev_node:
            print("There's no previous node")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_node(self,key):
        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        
        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next
        if curr_node == None:
            return
        prev.next = curr_node.next
        curr_node = None
