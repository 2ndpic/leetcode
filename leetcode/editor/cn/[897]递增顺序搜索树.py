# 给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [5,1,7]
# 输出：[1,null,5,null,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数的取值范围是 [1, 100] 
#  0 <= Node.val <= 1000 
#  
#  Related Topics 树 深度优先搜索 递归 
#  👍 175 👎 0
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def mid_order(node):
            if not node: return node
            mid_order(node.left)
            ans.append(node)
            mid_order(node.right)
        ans = []
        mid_order(root)
        ans.append(None)
        for i in range(len(ans) - 1):
            ans[i].right = ans[i + 1]
            ans[i].left = None
        return ans[0]
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        l = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            l.append(root)
            root = root.right
        dummy = TreeNode(-1)
        cur = dummy
        for node in l:
            cur.right = node
            cur.left = None
            cur = node
        return dummy.right

# leetcode submit region end(Prohibit modification and deletion)
