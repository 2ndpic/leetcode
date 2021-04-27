# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
# 输出：32
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [1, 2 * 104] 内 
#  1 <= Node.val <= 105 
#  1 <= low <= high <= 105 
#  所有 Node.val 互不相同 
#  
#  Related Topics 树 深度优先搜索 递归 
#  👍 189 👎 0
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def mid_order(node, cur):
            if not node: return cur
            cur = mid_order(node.left, cur)
            if low <= node.val <= high: cur += node.val
            cur = mid_order(node.right, cur)
            return cur

        return mid_order(root, 0

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack, ans = [], 0
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if low <= root.val <= high: ans += root.val
            root = root.right
        return ans

# leetcode submit region end(Prohibit modification and deletion)
