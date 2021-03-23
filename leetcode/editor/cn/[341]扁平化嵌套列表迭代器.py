# 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。 
# 
#  列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [[1,1],2,[1,1]]
# 输出: [1,1,2,1,1]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。 
# 
#  示例 2: 
# 
#  输入: [1,[4,[6]]]
# 输出: [1,4,6]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
#  
#  Related Topics 栈 设计 
#  👍 229 👎 0
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack and (not self.stack[-1].isInteger):
            l = self.stack.pop().getList()
            for each in l[::-1]:
                self.stack.append(each)
        return self.stack != []

# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
import collections
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = collections.deque()
        self._dfs(nestedList)

    def next(self) -> int:
        return self.queue.popleft()
    
    def hasNext(self) -> bool:
        return len(self.queue) != 0

    def _dfs(self, nests):
        for nest in nests:
            if nest.isInteger():
                self.queue.append(nest.getInteger())
            else:
                self._dfs(nest.getList())

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# leetcode submit region end(Prohibit modification and deletion)
