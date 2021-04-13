# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。 
# 
#  注意：本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bs
# t/ 相同 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：root = [4,2,6,1,3]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [2, 100] 内 
#  0 <= Node.val <= 105 
#  
#  
#  
#  Related Topics 树 深度优先搜索 递归 
#  👍 131 👎 0
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        """
        中序遍历就是有序的序列
        """
        def mid_order(node):
            if not node: return
            mid_order(node.left)
            arr.append(node.val)
            mid_order(node.right)
        arr = []
        mid_order(root)
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            diff = min(diff, arr[i] - arr[i - 1])
        return diff
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        """
        递归版
        """
        def dfs(node):
            nonlocal prev, ans
            if not node: return
            dfs(node.left)
            if prev:
                ans = min(ans, abs(prev.val - node.val))
            prev = node
            dfs(node.right)

        ans = 10 ** 5
        prev = None
        dfs(root)
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        """
        迭代版
        """
        ans = 10 ** 5
        prev = None
        stack = []
        while root or len(stack):
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev: ans = min(ans, abs(prev.val - root.val))
            prev = root
            root = root.right
        return ans
# leetcode submit region end(Prohibit modification and deletion)
