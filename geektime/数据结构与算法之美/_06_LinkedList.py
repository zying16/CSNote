# -*- coding: utf-8 -*-
"""
单链表的Python实现
"""

class Node:
    """
    链表中的Node结点
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkedList:
    """
    """
    def __init__(self, head=None):
        self.head = head

    def find_by_value(self, value):
        node = self.head
        while node and node.value != value:
            node = node.next
        return node

    def find_by_index(self, index):
        current = self.head
        pos = 0
        while current and pos != index:
            current = current.next
            pos += 1
        return current

    def insert_value_to_head(self, value):
        new_node = Node(value)
        self.insert_node_to_head(new_node)

    def insert_node_to_head(self, new_node):
        if new_node:
            new_node.next = self.head
            self.head = new_node

    def insert_node_to_tail(self, new_node):
        if not new_node:
            return
        if self.head is None:
            self.insert_node_to_head(new_node)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.next = None

    def insert_value_after(self, node, value):
        new_node = Node(value)
        self.insert_node_after(node, new_node)

    def insert_node_after(self, node, new_node):
        if node and new_node:
            new_node.next = node.next
            node.next = new_node

    def insert_value_before(self, node, value):
        new_node = Node(value)
        self.insert_node_before(node, new_node)

    def insert_node_before(self, node, new_node):
        # node and self.head should be allowed to be None in this case
        # node is None : insert_node_to_tail
        # self.head is None : insert_node_to_head
        if not new_node:
            return
        if node == self.head:
            self.insert_node_to_head(new_node)
            return
        if node is None:
            self.insert_node_to_tail(new_node)
            return
        current = self.head
        while current.next and current.next != node:
            current = current.next
        if current.next is None:
            return
        current.next = new_node
        new_node.next = node

    def delete_by_node(self, node):
        if node is None:
            return
        # if node is the head, should treat it specially
        if node == self.head:
            self.head = self.head.next
            return
        # if node.next not None, copy next value in this node and escape next node
        # advantage :  no need to loop through the list
        if node.next is not None:
            node.value = node.next.value
            node.next = node.next.next
            return
        # if node is the last one or not in the list
        current = self.head
        while current and current.next != node:
            current = current.next
        if current is None: # not in the list
             return
        current.next = node.next

    def delete_by_value1(self, value):
        node = self.find_by_value(value)
        self.delete_by_node(node)

    def delete_by_value(self, value):
        current = self.head
        # if value is self.head.value
        if current.value == value:
            self.head = current.next
            return
        # until to last item's previous one
        prev = None
        while current:
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def __repr__(self):
        nums = []
        current = self.head
        while current:
            nums.append(str(current.value))
            current = current.next
        return '->'.join(nums)

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def print_all(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()



if __name__ == "__main__":
    l = SingleLinkedList()
    for i in range(5):
        l.insert_value_to_head(i)
    assert repr(l) == '4->3->2->1->0'
    node3 = l.find_by_value(3)
    l.insert_value_before(node3, 10)
    assert repr(l) == '4->10->3->2->1->0'
    l.insert_value_after(node3, 11)
    assert repr(l) == '4->10->3->11->2->1->0'
    l.delete_by_value(2)
    assert repr(l) == '4->10->3->11->1->0'
    l.delete_by_value(0)
    assert repr(l) == '4->10->3->11->1'
    node10 = l.find_by_value(10)
    l.delete_by_node(node10)
    assert repr(l) == '4->3->11->1'
    l.delete_by_node(l.head)
    assert repr(l) == '3->11->1'
