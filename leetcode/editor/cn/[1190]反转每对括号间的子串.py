# 给出一个字符串 s（仅含有小写英文字母和括号）。 
# 
#  请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。 
# 
#  注意，您的结果中 不应 包含任何括号。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "(abcd)"
# 输出："dcba"
#  
# 
#  示例 2： 
# 
#  输入：s = "(u(love)i)"
# 输出："iloveu"
#  
# 
#  示例 3： 
# 
#  输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
#  
# 
#  示例 4： 
# 
#  输入：s = "a(bcdefghijkl(mno)p)q"
# 输出："apmnolkjihgfedcbq"
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 2000 
#  s 中只有小写英文字母和括号 
#  我们确保所有括号都是成对出现的 
#  
#  Related Topics 栈 
#  👍 94 👎 0
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ")":
                stack.append(i)
            elif i == ")":
                tmp = ""
                while True:
                    c = stack.pop()
                    if c == "(":
                        break
                    tmp += c
                stack.extend(list(tmp))
        return "".join(stack)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, cur = [], ""
        for i in s:
            if i == "(":
                stack.append(cur)
                cur = ""
            elif i == ")":
                cur = stack.pop() + cur[::-1]
            else:
                cur += i
        return cur


# leetcode submit region end(Prohibit modification and deletion)
s = "(abcd)"
s = "(u(love)i)"
# s = "(ed(et(oc))el)"
# s = "a(bcdefghijkl(mno)p)q"
print(Solution().reverseParentheses(s))