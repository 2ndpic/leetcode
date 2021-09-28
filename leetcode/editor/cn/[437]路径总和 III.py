# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。 
# 
#  路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：3
#  
# 
#  
# 
#  提示: 
# 
#  
#  二叉树的节点个数的范围是 [0,1000] 
#  -10⁹ <= Node.val <= 10⁹ 
#  -1000 <= targetSum <= 1000 
#  
#  Related Topics 树 深度优先搜索 二叉树 👍 1059 👎 0
class Solution:
    def dfs(self, node, target):
        ans = 0
        if node is None: return ans
        if node.val == target: ans += 1
        ans += self.dfs(node.left, target - node.val)
        ans += self.dfs(node.right, target - node.val)
        return ans

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if root is None: return 0
        return self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum) + self.dfs(root, targetSum)
from collections import defaultdict
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, curr):
            if not node: return 0
            ans = 0
            curr += node.val
            ans += prefix[curr - targetSum]
            prefix[curr] += 1
            ans += dfs(node.left, curr)
            ans += dfs(node.right, curr)
            prefix[curr] -= 1
            return ans
        prefix = defaultdict(int) # key是保存的前缀和，val是前缀和个数
        return dfs(root, 0)

# leetcode submit region end(Prohibit modification and deletion)
