# 给定一个正整数，返回它在 Excel 表中相对应的列名称。 
# 
#  例如， 
# 
#      1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#     ...
#  
# 
#  示例 1: 
# 
#  输入: 1
# 输出: "A"
#  
# 
#  示例 2: 
# 
#  输入: 28
# 输出: "AB"
#  
# 
#  示例 3: 
# 
#  输入: 701
# 输出: "ZY"
#  
#  Related Topics 数学 字符串 
#  👍 361 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber:
            if columnNumber == 26:
                ch = "Z"
                ans = ch + ans
                break
            ch = chr(columnNumber % 26 - 1 + ord('A'))
            ans = ch + ans
            columnNumber //= 26
        return ans
# leetcode submit region end(Prohibit modification and deletion)
columnNumber = 52
print(Solution().convertToTitle(columnNumber))