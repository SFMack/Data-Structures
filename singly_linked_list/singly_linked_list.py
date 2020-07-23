# create a node class that will be used to create the collection of nodes using the linked list structure
class Node:
    # set initial values for `value` and `next_node`
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

        # return the value of the current node
        def get_value(self):
            return self.value

        # return the value of the next node
        def get_next(self):
            return self.next_node

        # set the value of the next node using `new_next`
        def set_next(self, new_next):
            self.next_node = new_next

# the linked list itself only keeps track of the head and tail node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # 1. create a new node with the value argument
        new_node = Node(value, None)
        # 2. check to see if list is empty
        if not self.head:
            # if the list is empty, set head and tail to new node
            self.head = new_node
            self.tail = new_node
        else:
            # if the list is not empty
            # use the `set_next` method on the current tail node
            # to change the value of `next_node` -> our new node
            self.tail.set_next(new_node)
            # update the linkedlist `tail` to point to our new node
            self.tail = new_node

    def remove_head(self):
        # if there is no element in the list
        if not self.head:
            return None
        # if head has no next (aka one element in the list)
        if not self.head.get_next:
            # get reference to the head of the list
            head = self.head
            # remove the previous head
            self.head = None
            # remove tail reference
            self.tail = None
            # return head value
            return head.get_value()
        # change value
        value = self.head.get_value()
        # set the head reference to the a reference of the next node
        self.head = self.head.get_next()
        # return value
        return value
