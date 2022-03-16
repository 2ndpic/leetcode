# 请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。 
# 
#  实现 AllOne 类： 
# 
#  
#  AllOne() 初始化数据结构的对象。 
#  inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。 
#  dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。测试用例
# 保证：在减少计数前，key 存在于数据结构中。 
#  getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。 
#  getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", 
# "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# 输出
# [null, null, null, "hello", "hello", null, "hello", "leet"]
# 
# 解释
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // 返回 "hello"
# allOne.getMinKey(); // 返回 "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // 返回 "hello"
# allOne.getMinKey(); // 返回 "leet"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= key.length <= 10 
#  key 由小写英文字母组成 
#  测试用例保证：在每次调用 dec 时，数据结构中总存在 key 
#  最多调用 inc、dec、getMaxKey 和 getMinKey 方法 5 * 10⁴ 次 
#  
#  Related Topics 设计 哈希表 链表 双向链表 👍 196 👎 0

from collections import deque
import heapq
# leetcode submit region begin(Prohibit modification and deletion)
class Node:
    def __init__(self, key="", count=0):
        self.prev = self.next = None
        self.keys = {key}
        self.count = count

    def insert(self, node):
        # 在self后插入node
        node.prev = self
        node.next = self.next
        self.next = node
        node.next.prev = node
        return node

    def remove(self):
        # 从链表中移除self
        self.prev.next = self.next
        self.next.prev = self.prev

class AllOne:

    def __init__(self):
        self.root = Node()
        self.root.prev = self.root
        self.root.next = self.root # 初始化链表哨兵
        self.nodes = {}

    def inc(self, key: str) -> None:
        if key not in self.nodes:
            if self.root.next is self.root or self.root.next.count > 1:
                self.nodes[key] = self.root.insert(Node(key, 1))
            else:
                self.root.next.keys.add(key)
                self.nodes[key] = self.root.next
        else:
            cur = self.nodes[key]
            nxt = cur.next
            if nxt is self.root or nxt.count > cur.count + 1:
                self.nodes[key] = cur.insert(Node(key, cur.count + 1))
            else:
                nxt.keys.add(key)
                self.nodes[key] = nxt
            cur.keys.remove(key)
            if not cur.keys:
                cur.remove()

    def dec(self, key: str) -> None:
        cur = self.nodes[key]
        if cur.prev.count < cur.count - 1:
            self.nodes[key] = cur.prev.insert(Node(key, cur.count - 1))
        elif cur.count != 1:
            cur.prev.keys.add(key)
            self.nodes[key] = cur.prev
        else:
            del self.nodes[key]

        cur.keys.remove(key)
        if not cur.keys:
            cur.remove()

    def getMaxKey(self) -> str:
        return next(iter(self.root.prev.keys)) if self.root.prev is not self.root else ""

    def getMinKey(self) -> str:
        return next(iter(self.root.next.keys)) if self.root.next is not self.root else ""



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# leetcode submit region end(Prohibit modification and deletion)
