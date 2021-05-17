# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。 
# 
#  如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。 
# 
#  我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。 
# 
#  只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。 
# 
#  
# 
#  示例 1： 
#  
# 
#  
# 输入：root = [1,2,3,4], x = 4, y = 3
# 输出：false
#  
# 
#  示例 2： 
#  
# 
#  
# 输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
# 输出：true
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：root = [1,2,3,null,4], x = 2, y = 3
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  二叉树的节点数介于 2 到 100 之间。 
#  每个节点的值都是唯一的、范围为 1 到 100 的整数。 
#  
# 
#  
#  Related Topics 树 广度优先搜索 
#  👍 149 👎 0

import collections
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        BFS
        """
        q = collections.deque()
        q.append(root)
        tmp = [x, y]
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left and node.right:
                    if [node.left.val, node.right.val] == [x, y] or [node.left.val, node.right.val] == [y, x]:
                        return False
                if node.left:
                    q.append(node.left)
                    if node.left.val in tmp: tmp.remove(node.left.val)
                if node.right:
                    q.append(node.right)
                    if node.right.val in tmp: tmp.remove(node.right.val)
            if len(tmp) == 0: return True
            if len(tmp) == 1: return False
        return False

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        DFS
        返回值 父节点 和 递归深度
        -1 表示搜索不到 t
        0 表示搜索到了t，但是没有父节点
        """
        def dfs(node, fa, depth, t):
            if node is None: return [-1, -1]
            if node.val == t:
                return [fa.val if fa else 0, depth]
            l = dfs(node.left, node, depth + 1, t)
            if l[0] != -1: return l
            return dfs(node.right, node, depth + 1, t)
        xi = dfs(root, None, 0, x)
        yi = dfs(root, None, 0, y)
        return xi[0] != yi[0] and xi[1] == yi[1]
        
# leetcode submit region end(Prohibit modification and deletion)
