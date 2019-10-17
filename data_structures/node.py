# Linked-list is list connected to another list

"""
https://visualgo.net/en/list   # visualization of data structures

Node
data = <....>
next -> Node
LinkedList
----------
    self.head
    len()
    add()
    remove()
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def edit_data(self, new_value):
        self.data = new_value

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node

        

