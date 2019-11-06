class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._size = k
        self._len = 0
        self._deque = [0] * self._size


    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        print(self._len)
        for i in range(self._len):
            print(i)
            self._deque[self._len - i] = self._deque[self._len - i - 1]
        self._deque[0] = value
        self._len += 1
        return True


    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self._deque[self._len] = value
        self._len += 1
        return True


    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        for i in range(self._len - 1):
            self._deque[i] = self._deque[i + 1]
        self._len -= 1
        return True



    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self._deque[self._len - 1] = 0
        self._len -= 1
        return True


    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self._deque[0]


    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self._deque[self._len - 1]



    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self._len == 0


    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self._len == self._size


circularDeque = MyCircularDeque(3)
assert True == circularDeque.insertLast(1)
assert True == circularDeque.insertLast(2)
assert True == circularDeque.insertFront(3)
assert False == circularDeque.insertFront(4)
assert circularDeque.getRear() == 2
assert circularDeque.isFull() == True
print(circularDeque._deque)
assert circularDeque.deleteLast() == True
print(circularDeque._deque)
assert circularDeque.insertFront(4) == True
