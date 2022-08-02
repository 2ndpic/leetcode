# leetcode submit region begin(Prohibit modification and deletion)
class Node:

    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        if k <= 0:
            self.font_point = None
            self.rear_point = None
        else:
            head = Node()
            curr = head
            for _ in range(k - 1):
                node = Node()
                curr.next = node
                curr = node
            curr.next = head
            self.font_point = head
            self.rear_point = head
        self.rear_val = -1
        self.count = 0
        self.k = k


    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.rear_point.val = value
        self.rear_point = self.rear_point.next
        self.count += 1
        self.rear_val = value
        return True


    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.font_point.val = -1
        self.font_point = self.font_point.next
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.font_point.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.rear_val


    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k

class MyCircularQueue:

    def __init__(self, k: int):
        self.elements = [0] * (k + 1)
        self.font = self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.elements[self.rear] = value
        self.rear = (self.rear + 1) % len(self.elements)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.font = (self.font + 1) % len(self.elements)
        return True

    def Front(self) -> int:
        return self.elements[self.font] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.elements[(self.rear - 1) % len(self.elements)] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.rear == self.font

    def isFull(self) -> bool:
        return ((self.rear + 1) % len(self.elements)) == self.font

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# leetcode submit region end(Prohibit modification and deletion)
