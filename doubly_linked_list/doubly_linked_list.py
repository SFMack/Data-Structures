"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        # if theres a reference to a prev node
        if self.prev:
            # change the previous nodes next value to be the next node reference
            self.prev.next = self.next
        # if theres a reference to a next node
        if self.next:
            # change the next nodes previous value to be the previous node reference
            self.next.prev = self.prev


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        # if the list is empty
        if not self.head and not self.tail:
            # set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # on the new node, set the next node to the current head node
            new_node.next = self.head
            # on the current head node, set the previous node to the new node
            self.head.prev = new_node
            # set the current head to the new node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # get head's value
        value = self.head.value
        # call delete on head
        self.delete(self.head)
        # return the value
        return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        # if list is empty
        if not self.tail and not self.head:
            # set head and tail to the new node
            self.tail = new_node
            self.head = new_node
        else:
            # set the new node's prev node reference to the current tail
            new_node.prev = self.tail
            # set the current tail node's next node reference to the new node
            self.tail.next = new_node
            # set the tail node reference to the new node
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if not self.head:
            return None
        # get tail's value
        value = self.tail.value
        # call delete on tail
        self.delete(self.tail)
        # return the value
        self.tail = self.tail.prev
        return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # is node at the head
        if node.value is self.head.value:
            # do nothing
            return None
        # capture the value of the current node
        value = node.value
        # if the node is at the tail
        if node.value is self.tail.value:
            # remove from tail
            self.remove_from_tail()
        # otherwise
        else:
            # delete node
            node.delete()
            # decrement length
            self.length -= 1
        # use add_to_head to put the node at the front of the list
        self.add_to_head(value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        # is node at the tail
        if node is self.tail:
            # do nothing
            return
        # capture the value of the current node
        value = node.value
        # if the node is at the head
        if node is self.head:
            # remove from head
            self.remove_from_head()
        # otherwise
        else:
            # delete node
            node.delete()
            # derement length
            self.length -= 1
            # use add_to_tail to put the node at the end of the list
            self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        prev_node = node.prev
        next_node = node.next
        if node is self.head:
            self.remove_from_head
        elif node is self.tail:
            self.remove_from_tail
        node.delete()
        self.length -= 1
        return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if not self.head:
            return None
        current = self.head
        max_val = self.head.value
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val
