from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans, best, cur = 0, float('-inf'), 0
        while q:
            cur += 1
            cur_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                cur_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if cur_sum > best:
                best = cur_sum
                ans = cur
        return ans
# leetcode submit region end(Prohibit modification and deletion)
