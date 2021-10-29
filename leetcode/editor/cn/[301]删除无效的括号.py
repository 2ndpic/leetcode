# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。 
# 
#  返回所有可能的结果。答案可以按 任意顺序 返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "()())()"
# 输出：["(())()","()()()"]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "(a)())()"
# 输出：["(a())()","(a)()()"]
#  
# 
#  示例 3： 
# 
#  
# 输入：s = ")("
# 输出：[""]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 25 
#  s 由小写英文字母以及括号 '(' 和 ')' 组成 
#  s 中至多含 20 个括号 
#  
#  Related Topics 广度优先搜索 字符串 回溯 👍 612 👎 0
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def checkValid(str, lmask, left, rmask, right):
            pos1, pos2 = 0, 0
            cnt = 0

            for i in range(len(str)):
                if pos1 < len(left) and i == left[pos1]:
                    if lmask & (1 << pos1) == 0:
                        cnt += 1
                    pos1 += 1
                elif pos2 < len(right) and i == right[pos2]:
                    if rmask & (1 << pos2) == 0:
                        cnt -= 1
                        if cnt < 0:
                            return False
                    pos2 += 1

            return cnt == 0

        def recoverStr(lmask, left, rmask, right):
            pos1, pos2 = 0, 0
            res = ""

            for i in range(len(s)):
                if pos1 < len(left) and i == left[pos1]:
                    if lmask & (1 << pos1) == 0:
                        res += s[i]
                    pos1 += 1
                elif pos2 < len(right) and i == right[pos2]:
                    if rmask & (1 << pos2) == 0:
                        res += s[i]
                    pos2 += 1
                else:
                    res += s[i]

            return res

        def countBit(x):
            res = 0
            while x != 0:
                x = x & (x - 1)
                res += 1
            return res

        lremove, rremove = 0, 0
        left, right = [], []
        ans = []
        cnt = set()

        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
                lremove += 1
            elif s[i] == ')':
                right.append(i)
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

        m, n = len(left), len(right)
        maskArr1, maskArr2 = [], []
        for i in range(1 << m):
            if countBit(i) != lremove:
                continue
            maskArr1.append(i)
        for i in range(1 << n):
            if countBit(i) != rremove:
                continue
            maskArr2.append(i)
        for mask1 in maskArr1:
            for mask2 in maskArr2:
                if checkValid(s, mask1, left, mask2, right):
                    cnt.add(recoverStr(mask1, left, mask2, right))

        return [val for val in cnt]


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        ans = []
        currSet = set([s])

        while True:
            for ss in currSet:
                if isValid(ss):
                    ans.append(ss)
            if len(ans) > 0:
                return ans
            nextSet = set()
            for ss in currSet:
                for i in range(len(ss)):
                    if i > 0 and ss[i] == s[i - 1]:
                        continue
                    if ss[i] == '(' or ss[i] == ')':
                        nextSet.add(ss[:i] + ss[i + 1:])
            currSet = nextSet
        return ans

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def check():
            l, r, tmp = 0, 0, "".join([i for i, j in zip(s, remove_state) if j == False])
            for i in tmp:
                if i == "(": l += 1
                elif i == ")": r += 1
                if r > l: return None
            return tmp if l == r else None

        def backtracking(start, lr, rr):
            if lr == rr == 0:
                tmp = check()
                if (tmp := check()) is not None:
                    ans.append(tmp)
                return
            for i in range(start, n):
                if i > start and s[i] == s[i-1]: continue
                if lr + rr > n - i: break
                remove_state[i] = True
                if s[i] == "(" and lr > 0: backtracking(i + 1, lr - 1, rr)
                elif s[i] == ")" and rr > 0: backtracking(i + 1, lr, rr - 1)
                remove_state[i] = False

        lremove, rremove, n = 0, 0, len(s)
        remove_state = [False] * n
        for i in s:
            if i == "(": lremove += 1
            elif i == ")":
                if lremove: lremove -= 1
                else: rremove += 1
        ans = []
        backtracking(0, lremove, rremove)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
s = ")("
print(Solution().removeInvalidParentheses(s))