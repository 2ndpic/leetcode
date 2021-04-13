# 小扣有一个根结点为 `root` 的二叉树模型，初始所有结点均为白色，可以用蓝色染料给模型结点染色，模型的每个结点有一个 `val` 价值。小扣出于美观考虑
# ，希望最后二叉树上每个蓝色相连部分的结点个数不能超过 `k` 个，求所有染成蓝色的结点价值总和最大是多少？
# 
# 
# **示例 1：**
# > 输入：`root = [5,2,3,4], k = 2`
# >
# > 输出：`12`
# >
# > 解释：`结点 5、3、4 染成蓝色，获得最大的价值 5+3+4=12`
# ![image.png](https://pic.leetcode-cn.com/1616126267-BqaCRj-image.png)
# 
# 
# **示例 2：**
# > 输入：`root = [4,1,3,9,null,null,2], k = 2`
# >
# > 输出：`16`
# >
# > 解释：结点 4、3、9 染成蓝色，获得最大的价值 4+3+9=16
# ![image.png](https://pic.leetcode-cn.com/1616126301-gJbhba-image.png)
# 
# 
# 
# **提示：**
# + `1 <= k <= 10`
# + `1 <= val <= 10000`
# + `1 <= 结点数量 <= 10000`
#  👍 3 👎 0
class Solution:
    def maxValue(self, root: TreeNode, k: int) -> int:
        """
        超时了
        """
        def dfs(node, i):
            ans = 0
            if not node: return ans
            if i == 0: return self.maxValue(node.left, k) + self.maxValue(node.right, k)
            for j in range(i):
                ans = max(ans, node.val + dfs(node.left, j) + dfs(node.right, i - j - 1))
            return ans

        ans = 0
        if not root: return ans
        for i in range(k + 1):
            ans = max(ans, dfs(root, i))
        return ans
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxValue(self, root: TreeNode, k: int) -> int:
        """
        递归
        定义f[i]表示以该节点为根，相邻子节点染色的个数为i（包含自身）的情况下，节点价值总和的最大值; 0 <= i <= k
        i == 0: 表示当前根节点为白色，无所谓相邻子节点的颜色，f[0] = max(fl) + max(fr)
        i == 1: 表示当前根节点染色，且相邻子节点（左右孩子）都没有染色，f[1] = node.val + fl[0] + fr[0]
        i == 2: 表示当前根节点染色，且相邻子节点左右孩子有一个染色,f[2] = node.val + max(fl[1] + fr[0], fl[1] + fr[0])
        f[0] = max(fl) + max(fr) i = 0
        f[i] = node.val + max(fl[j] + fr[i - j - 1]) 0 < i <= k and 0 <= j < i
        初始状态：当前节点为空，f[i] = 0 (0 <= i <= k)
        最终结果：根节点所有情况的最大值，max(f)
        """
        def dfs(root):
            f = [0] * (k + 1)
            if not root: return f
            fl, fr = dfs(root.left), dfs(root.right)
            f[0] = max(fl) + max(fr)
            for i in range(1, k + 1):
                for j in range(i):
                    f[i] = max(f[i], root.val + fl[j] + fr[i - j - 1])
            return f
        return max(dfs(root))
# leetcode submit region end(Prohibit modification and deletion)
# [5,2,3,4]
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
print(Solution().maxValue(root, 2))