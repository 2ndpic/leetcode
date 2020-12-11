# 给定一个Excel表格中的列名称，返回其相应的列序号。 
# 
#  例如， 
# 
#      A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
#  
# 
#  示例 1: 
# 
#  输入: "A"
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入: "AB"
# 输出: 28
#  
# 
#  示例 3: 
# 
#  输入: "ZY"
# 输出: 701 
# 
#  致谢： 
# 特别感谢 @ts 添加此问题并创建所有测试用例。 
#  Related Topics 数学 
#  👍 179 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def titleToNumber(self, s: str) -> int:
        '''
        就是一个简单的进制问题，26进制转10进制
        '''
        ret = 0
        for i in range(len(s)):
            ret = ret * 26 + (ord(s[i]) - ord('A') + 1)
        return ret

# leetcode submit region end(Prohibit modification and deletion)
