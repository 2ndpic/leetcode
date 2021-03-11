# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。 
# 
#  整数除法仅保留整数部分。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "3+2*2"
# 输出：7
#  
# 
#  示例 2： 
# 
#  
# 输入：s = " 3/2 "
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：s = " 3+5 / 2 "
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 3 * 105 
#  s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开 
#  s 表示一个 有效表达式 
#  表达式中的所有整数都是非负整数，且在范围 [0, 231 - 1] 内 
#  题目数据保证答案是一个 32-bit 整数 
#  
#  
#  
#  Related Topics 栈 字符串 
#  👍 322 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        pre_op = "+"
        num = 0
        for idx, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if idx == len(s) - 1 or c in "+-*/":
                if pre_op == "+":
                    stack.append(num)
                elif pre_op == "-":
                    stack.append(-num)
                elif pre_op == "*":
                    stack.append(stack.pop() * num)
                elif pre_op == "/":
                    stack.append(int(stack.pop() / num))
                num = 0
                pre_op = c
        return sum(stack)

# leetcode submit region end(Prohibit modification and deletion)
s = " 5*5 / 25 * 6 + 1"
print(Solution().calculate(s))