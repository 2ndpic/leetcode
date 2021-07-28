# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。 
# 
#  返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# 输出：[7,4,1]
# 解释：
# 所求结点为与目标结点（值为 5）距离为 2 的结点，
# 值分别为 7，4，以及 1
# 
# 
# 
# 注意，输入的 "root" 和 "target" 实际上是树上的结点。
# 上面的输入仅仅是对这些对象进行了序列化描述。
#  
# 
#  
# 
#  提示： 
# 
#  
#  给定的树是非空的。 
#  树上的每个结点都具有唯一的值 0 <= node.val <= 500 。 
#  目标结点 target 是树上的结点。 
#  0 <= K <= 1000. 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 340 👎 0
from collections import deque, defaultdict
from typing import List
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node):
            if not node: return
            if node.left:
                g[node.val].append(node.left.val)
                g[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                g[node.val].append(node.right.val)
                g[node.right.val].append(node.val)
                dfs(node.right)
        g = defaultdict(list)
        dfs(root)
        q = deque([target.val])
        seen = {target.val}
        while q and k:
            for _ in range(len(q)):
                u = q.popleft()
                for v in g[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
            k -= 1
        return list(q)

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def findParents(node):
            if node.left:
                node.left.parent = node
                findParents(node.left)
            if node.right:
                node.right.parent = node
                findParents(node.right)
        def findAns(node, from_node, depth, k):
            if not node: return
            if depth == k:
                ans.append(node.val)
                return
            if node.left != from_node:
                findAns(node.left, node, depth + 1, k)
            if node.right != from_node:
                findAns(node.right, node, depth + 1, k)
            if node.parent != from_node:
                findAns(node.parent, node, depth + 1, k)

        root.parent, ans = None, []
        findParents(root)
        findAns(target, None, 0, k)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
