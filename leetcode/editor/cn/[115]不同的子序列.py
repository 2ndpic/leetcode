# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。 
# 
#  字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列
# ，而 "AEC" 不是） 
# 
#  题目数据保证答案符合 32 位带符号整数范围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
# (上箭头符号 ^ 表示选取的字母)
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^ 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length, t.length <= 1000 
#  s 和 t 由英文字母组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 342 👎 0

import functools
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @functools.lru_cache()
        def helper(i, j):
            """
            :param i: 以s[0],...,s[i]去匹配t[0],..,[j]的串的个数
            :param j:
            :return:
            """
            if i == -1 or j == -1:
                return 1 if i == j or i > -1 else 0
            if s[i] == t[j]:
                return helper(i - 1, j - 1) + helper(i - 1, j)
            return helper(i - 1, j)
        return helper(len(s) - 1, len(t) - 1)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        dp[i][j]表示s前i个字符t前j个字符的个数
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j] if s[i] == t[j]
        dp[i][j] = dp[i-1][j]
        """
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]+ dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][m]


# leetcode submit region end(Prohibit modification and deletion)
s = "babgbag"
t = "bag"
s = "rabbbit"
t = "rabbit"
s = "ccc"
t = "c"
print(Solution().numDistinct(s, t))
