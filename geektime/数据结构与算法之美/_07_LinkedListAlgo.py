from _06_LinkedList import Node, SingleLinkedList

"""
重点掌握五种常见的链表操作：
    单链表反转
    链表中环的检测
    两个有序链表的合并
    删除链表倒数第n个结点
    求链表的中间结点
"""

class LinkedListAlgo(SingleLinkedList):
    # 单链表反转
    def reverse2(self):
        reversed_head = None
        current = self.head
        while current:
            reversed_head, reversed_head.next, current = current, reversed_head, current.next
        self.head = reversed_head

    def reverse(self):
        current, prev = self.head, None
        while current:
            current.next, prev, current = prev, current, current.next
        self.head = prev

    # 链表中环的检测
    def has_cycle(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def remove_head(self):
        if not self.head:
            return
        self.head = self.head.next

    def remove_nth_from_start(self, n: int):
        if not self.head:
            return
        # if to remove the first node
        if n == 1:
            self.remove_head()
            return
        count = 0
        current = self.head
        prev = Node(None)
        while current and count < n :
            prev, current = current, current.next
            count += 1
        if count == n:
            prev.next = prev.next.next

    # 删除链表倒数第n个结点
    def remove_nth_from_end(self, n: int):
        if not self.head:
            return
        slow, fast = self.head, self.head
        count = 0
        while fast and count < n:
            fast = fast.next
            count += 1
        # not enough nodes
        if not fast and count < n:
            return
        # if nth_from_end is the first node from start to be removed
        if not fast and count == n:
            self.head = self.head.next
            return
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

    # 求链表的中间结点
    def find_mid_node(self):
        # if empty
        if not self.head:
            return self.head
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


def reversed(l: SingleLinkedList):
    reversed_head = None
    current = l.head
    while current:
        reversed_head, reversed_head.next, current = current, reversed_head, current.next
    return SingleLinkedList(reversed_head)

# 两个有序链表的合并
def merge_sorted_list(l1: SingleLinkedList, l2: SingleLinkedList):
    p1, p2 = l1.head, l2.head
    fake_head = Node(None)
    current = fake_head
    while p1 and p2:
        if p1.value < p2.value:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next
    current.next = p1 if p1 else p2
    return fake_head.next



if __name__ == "__main__":
    l = LinkedListAlgo()
    for i in range(5):
        l.insert_value_to_head(i)
    assert repr(l) == '4->3->2->1->0'
    l.reverse()
    assert repr(l) == '0->1->2->3->4'
    l = reversed(l)
    assert repr(l) == '4->3->2->1->0'
    l1 = LinkedListAlgo()
    for i in [5, 3, 2, 1]:
        l1.insert_value_to_head(i)
    assert repr(l1) == '1->2->3->5'
    l2 = LinkedListAlgo()
    for i in [6, 4, 0]:
        l2.insert_value_to_head(i)
    assert repr(l2) == '0->4->6'
    merged_list = SingleLinkedList(merge_sorted_list(l1, l2))
    assert repr(merged_list) == '0->1->2->3->4->5->6'
    l1 = LinkedListAlgo()
    for i in [1, 3, 4, 5]:
        l1.insert_value_to_head(i)
    l = LinkedListAlgo()
    for i in range(11):
        l.insert_value_to_head(i)
    assert repr(l) == '10->9->8->7->6->5->4->3->2->1->0'
    l.remove_nth_from_end(1)
    assert repr(l) == '10->9->8->7->6->5->4->3->2->1'
    l.remove_nth_from_end(5)
    assert repr(l) == '10->9->8->7->6->4->3->2->1'
    l.remove_nth_from_end(9)
    assert repr(l) == '9->8->7->6->4->3->2->1'
    l.remove_nth_from_end(10)
    assert repr(l) == '9->8->7->6->4->3->2->1'
    l = LinkedListAlgo()
    for i in range(11):
        l.insert_value_to_head(i)
    assert repr(l) == '10->9->8->7->6->5->4->3->2->1->0'
    mid_node = l.find_mid_node()
    assert mid_node.value == 5
    l.insert_value_to_head(11)
    assert repr(l) == '11->10->9->8->7->6->5->4->3->2->1->0'
    mid_node = l.find_mid_node()
    assert mid_node.value == 6
