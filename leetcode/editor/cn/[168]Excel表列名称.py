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
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber:
            rst = columnNumber % 26
            if rst == 0:
                rst = 26
            ch = chr(rst - 1 + ord("A"))
            ans = ch + ans
            columnNumber = (columnNumber - rst) // 26
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber:
            columnNumber -= 1
            ch = chr(columnNumber % 26 + ord("A"))
            ans += ch
            columnNumber //= 26
        return ans[::-1]
# leetcode submit region end(Prohibit modification and deletion)
columnNumber = 701
print(Solution().convertToTitle(columnNumber))