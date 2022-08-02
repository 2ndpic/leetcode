# leetcode submit region begin(Prohibit modification and deletion)
class Node:

    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = Node()
        self.inser_point = self.head
        self.pop_point = self.head
        curr = self.head
        for _ in range(k):
            node = Node()
            curr.next = node
            curr = node
    def enQueue(self, value: int) -> bool:
        tail = self.head.next.next
        if tail.val != -1:
            return False
        t


    def deQueue(self) -> bool:


    def Front(self) -> int:


    def Rear(self) -> int:


    def isEmpty(self) -> bool:


    def isFull(self) -> bool:



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# leetcode submit region end(Prohibit modification and deletion)
