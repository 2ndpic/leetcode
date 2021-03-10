# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "1 + 1"
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：s = " 2-1 + 2 "
# 输出：3
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 3 * 105 
#  s 由数字、'+'、'-'、'('、')'、和 ' ' 组成 
#  s 表示一个有效的表达式 
#  
#  Related Topics 栈 数学 
#  👍 425 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
def cal(arr):
    # 此arr数组只包含数字和+-符号,例如["2", "-", "1", "+", "2", "2"] 22 + 1 - 2
    ans = 0
    tmp = 0
    mi = 0
    for i in range(len(arr)):
        if arr[i] == "+":
            ans += tmp
            tmp = 0
            mi = 0
        elif arr[i] == "-":
            ans -= tmp
            tmp = 0
            mi = 0
        else:
            tmp += int(arr[i]) * (10 ** mi)
            mi += 1
    ans += tmp
    return ans

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s = "".join(s.split(" "))
        for i in s:
            tmp = []
            if i == ")":
                while True:
                    c = stack.pop()
                    if c == "(":
                        break
                    tmp.append(c)
                stack.append(cal(tmp))
            else:
                stack.append(i)
        return cal(stack[::-1])
# leetcode submit region end(Prohibit modification and deletion)
s = " -1 + 2 - 3 + 4 "
print(Solution().calculate(s))