# 请实现两个函数，分别用来序列化和反序列化二叉树。 
# 
#  你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字
# 符串反序列化为原始的树结构。 
# 
#  提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方
# 法解决这个问题。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
#  
# 
#  
# 
#  注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-b
# inary-tree/ 
#  Related Topics 树 深度优先搜索 广度优先搜索 设计 字符串 二叉树 
#  👍 213 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        arr = []
        q = collections.deque([root])
        while q:
            node = q.popleft()
            arr.append(node.val if node else None)
            if node is not None:
                q.append(node.left)
                q.append(node.right)
        return str(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]": return None
        data = [int(i.strip()) if i != " None" else None for i in data[1:-1].split(',')]
        root = TreeNode(data[0])
        q = collections.deque([root])
        i = 1
        while q:
            node = q.popleft()
            if data[i] is not None:
                node.left = TreeNode(data[i])
                q.append(node.left)
            i += 1
            if data[i] is not None:
                node.right = TreeNode(data[i])
                q.append(node.right)
            i += 1
        return root






# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
data = "[1, 2, 3, None, None, 4, 5, None, None, None, None]"
print(Codec().deserialize(data))