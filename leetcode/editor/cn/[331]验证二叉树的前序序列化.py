# 序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。 
# 
#       _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
#  
# 
#  例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。 
# 
#  给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。 
# 
#  每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。 
# 
#  你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。 
# 
#  示例 1: 
# 
#  输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# 输出: true 
# 
#  示例 2: 
# 
#  输入: "1,#"
# 输出: false
#  
# 
#  示例 3: 
# 
#  输入: "9,#,#,1"
# 输出: false 
#  Related Topics 栈 
#  👍 201 👎 0

import functools
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        递归超时版本
        """
        preorder = tuple(preorder.split(','))
        @functools.lru_cache()
        def valid(arr):
            if not arr:
                return False
            if len(arr) == 1:
                if arr[0] == "#":
                    return True
                return False
            if arr[0] == "#":
                return False
            for i in range(len(arr)):
                if arr[i] == "#":
                    if valid(arr[1:i + 1]) and valid(arr[i + 1:]):
                        return True
            return False
        return valid(preorder)
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        st = preorder.split(",")
        stack = []
        for i in st:
            stack.append(i)
            while len(stack) > 2 and stack[-2] == "#" and stack[-1] == "#":
                stack.pop()
                stack.pop()
                if stack[-1] == "#":
                    return False
                stack[-1] = "#"
        return stack == ["#"]

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        合法的二叉树所有节点的出度和==入度和
        空节点提供一个入度，0个出度
        非空节点提供一个入度，两个出度
        """
        degree = 1
        for i in preorder.split(','):
            degree -= 1
            if degree < 0: return False  # 度不够用了
            if i != "#": degree += 2
        return degree == 0

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        非空节点数量为 m，空节点数量为 n，在遍历没结束前恒成立：m>=n
        非空节点入度为1出度为2，空节点入度为1出度为0，初始化总入度为0总出度为1
        总入度为 m+n,总出度为2*m+1 可得 (2*m + 1)- (m+n) > 0
        故在遍历没有结束前总出度是一定大于总入度
        """
        ind, outd = 0, 1
        for i in preorder.split(','):
            if outd <= ind:
                return False
            ind += 1
            outd += 2 if i != "#" else 0
        return ind == outd
# leetcode submit region end(Prohibit modification and deletion)
s = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# s = "9,#,#,1"
# s = "#,#,3,5,#"
# s = "#,7,6,9,#,#,#"
print(Solution().isValidSerialization(s))