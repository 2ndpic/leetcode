# 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则： 
# 
#  
#  任何左括号 ( 必须有相应的右括号 )。 
#  任何右括号 ) 必须有相应的左括号 ( 。 
#  左括号 ( 必须在对应的右括号之前 )。 
#  * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。 
#  一个空字符串也被视为有效字符串。 
#  
# 
#  示例 1: 
# 
#  
# 输入: "()"
# 输出: True
#  
# 
#  示例 2: 
# 
#  
# 输入: "(*)"
# 输出: True
#  
# 
#  示例 3: 
# 
#  
# 输入: "(*))"
# 输出: True
#  
# 
#  注意: 
# 
#  
#  字符串大小将在 [1，100] 范围内。 
#  
#  Related Topics 栈 贪心 字符串 动态规划 👍 428 👎 0
class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        dp[i][j]表示s[i,..,j]是否是有效的括号字符串 其中 0 <= i <= j < n
        当子串长度为1时，只有*才是有效的，表示空字符串
        当子串长度为2时，只有() (* *) ** 是有效的
        当子串长度大于2， 即 j - i + 1 > 2 即 j - i >= 2时
        - 如果s[i]s[j] == () (* *) **, dp[i][j] = dp[i + 1][j - 1]
        - 如果存在k, i <= k < j将s[i...j]分成s[i,..,k]和s[k+1,...,j] 那么dp[i][j] = dp[i][k] | dp[k + 1][j]
        最终答案是dp[0][n-1]
        主要dp[i][j]的答案由dp[i][k],dp[i+1][j-1], dp[k+1][j]更新得来，所以要注意计算顺序
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            if s[i] == '*': dp[i][i] = True
        for i in range(n - 1):
            dp[i][i + 1] = s[i] in "(*" and s[i+1] in ")*"
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                if s[i] in "(*" and s[j] in ")*": dp[i][j] = dp[i + 1][j - 1]
                for k in range(i, j):
                    dp[i][j] |= dp[i][k] and dp[k + 1][j]
        return dp[0][n - 1]

class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        两个栈，左括号栈l和星号栈x，遇到右括号时
        - if ll.pop()
        - if x: x.pop()
        - else: return False
        遍历结束后左括号栈l和星号栈x可能还有元素，为了将每个左括号匹配，需要将星号看成右括号，且每个左括号必须出现在其匹配的星号前
        最终判断左括号栈是否为空，如果为空就匹配完毕，剩下的星号都可以看作空字符串，返回True
        """
        l, x = [], []
        for i, ch in enumerate(s):
            if ch == "(": l.append(i)
            elif ch == "*": x.append(i)
            elif l: l.pop()
            elif x: x.pop()
            else: return False

        while l and x:
            l_idx, x_idx = l.pop(), x.pop()
            if x_idx < l_idx: return False
        return l == []

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        贪心可将空间复杂度降为O(1)
        从左到右遍历字符串，未匹配的左括号数可能出现如下变化：
        - 如果遇到左括号，则未匹配的左括号数加1
        - 如果遇到右括号，则需要一个左括号匹配，未匹配的左括号数减1
        - 如果遇到星号，可以看出左括号右括号空字符，因此左括号的数量可能加一减一或不变
        基于上诉结论，可以在遍历过程中维护左括号数量的最小值和最大值，根据遍历到的字符更新最小值和最大值
        - 如果遇到左括号，则将最大值最小值都加1
        - 如果遇到右括号，则将最大值最小值都减1
        - 如果遇到星号，则将最小值减1，最大值加1
        任何情况下，未匹配的左括号数量都必须大于等于0，因此最大值<0时,return False
        当最小值为0时，不应将最小值继续减少，以确保最小值非负
        遍历结束时，所有的左括号都应和右括号匹配，因此只有当最小值为0时，字符串s才是最有效的括号字符串
        """
        mi, ma = 0, 0
        for ch in s:
            if ch == "(":
                mi += 1
                ma += 1
            elif ch == ")":
                mi = max(mi - 1, 0)
                ma -= 1
            else:
                mi = max(mi - 1, 0)
                ma += 1
            if ma < 0: return False
        return mi == 0
# leetcode submit region end(Prohibit modification and deletion)
