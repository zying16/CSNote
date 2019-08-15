class ListStack:
    def __init__(self, n: int):
        self.items = []
        self._capacity = n
        self.count = 0

    def push(self, item):
        if self.count >= self._capacity:
            return
        self.items.append(item)
        self.count += 1

    def pop(self):
        if self.count == 0:
            return False
        tmp = self.items.pop()
        self.count -= 1
        return tmp


if __name__ == '__main__':
    l = ListStack(5)
    assert l.items == []
    l.push(1)
    assert l.items == [1]
    l.push(2)
    assert l.items == [1, 2]
    t = l.pop()
    assert t == 2
    assert l.items == [1]
    l.push(3)
    assert l.items == [1, 3]
