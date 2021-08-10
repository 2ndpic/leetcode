# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。 
# 
#  你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点
# 。 
# 
#  示例 1: 
# 
#  
# 输入: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# 输出: 
# 合并后的树:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7
#  
# 
#  注意: 合并必须从两个树的根节点开始。 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 747 👎 0
from collections import deque
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 or not root2: return root1 | root2
        root1.val += root2.val
        l = self.mergeTrees(root1.left, root2.left)
        r = self.mergeTrees(root1.right, root2.right)
        root1.left, root1.right = l, r
        return root1

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 or not root2: return root1 or root2
        q = deque([(root1, root2)])
        while q:
            t1, t2 = q.popleft()
            t1.val += t2.val
            if t1.left and t2.left:
                q.append((t1.left, t2.left))
            elif not t1.left:
                t1.left = t2.left
            if t1.right and t2.right:
                q.append((t1.right, t2.right))
            elif not t1.right:
                t1.right = t2.right
        return root1

# leetcode submit region end(Prohibit modification and deletion)
