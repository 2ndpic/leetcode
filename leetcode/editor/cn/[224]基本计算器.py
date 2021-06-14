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

class Solution:
    def calculate(self, s: str) -> int:
        ops = [1]  # 栈顶记录当前位置所处的[所有括号]所[共同形成]的符号
        sign = 1   # 代表当前位置的符号
        ret = 0
        i, n = 0, len(s)
        while i < n:
            if s[i] == " ":
                i += 1
            elif s[i] == "+":
                sign = ops[-1]
                i += 1
            elif s[i] == "-":
                sign = -ops[-1]
                i += 1
            elif s[i] == "(":
                ops.append(sign)
                i += 1
            elif s[i] == ")":
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord("0")
                    i += 1
                ret += num * sign
        return ret


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        """
        双栈解法
        """
        st_num, st_signs = [], []
        ans, sign, n = 0, 1, len(s)
        i = 0
        while i < n:
            if s[i] == " ":
                i += 1
            elif s[i] == "+" or s[i] == "-":
                sign = 1 if s[i] == "+" else -1
                i += 1
            elif s[i] == "(":
                st_num.append(ans)
                st_signs.append(sign)
                ans = 0
                sign = 1
                i += 1
            elif s[i] == ")":
                ans = st_num.pop() + st_signs.pop() * ans
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord("0")
                    i += 1
                ans += (sign * num)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
# s = " -1 + 2 - 3 + 4 "
s = "1+2+(3-(4+5))"
print(Solution().calculate(s))