# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下： 
# 
#  
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# } 
# 
#  填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。 
# 
#  初始状态下，所有 next 指针都被设置为 NULL。 
# 
#  
# 
#  进阶： 
# 
#  
#  你只能使用常量级额外空间。 
#  使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。 
#  
# 
#  
# 
#  示例： 
# 
#  
# 
#  
# 输入：root = [1,2,3,4,5,6,7]
# 输出：[1,#,2,3,#,4,5,6,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 
# next 指针连接，'#' 标志着每一层的结束。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数量少于 4096 
#  -1000 <= node.val <= 1000 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 516 👎 0
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i < size - 1:
                    node.next = q[0]
                if node.left:
                    q.extend([node.left, node.right])
        return root

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left: return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        第N层建立next指针后再建立N+1层的next指针
        """
        if not root: return root
        leftmost = root
        while leftmost.left:
            # 遍历这一层节点组织成的链表（已经添加好next了）,为下一层更新next指针
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root
# leetcode submit region end(Prohibit modification and deletion)
