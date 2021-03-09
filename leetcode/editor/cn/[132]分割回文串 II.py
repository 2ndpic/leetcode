# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。 
# 
#  返回符合要求的 最少分割次数 。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "ab"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 2000 
#  s 仅由小写英文字母组成 
#  
#  
#  
#  Related Topics 动态规划 
#  👍 386 👎 0

class Solution:
    def minCut(self, s: str) -> int:
        """
        dp[i]定义为以s第i个字符结尾的字符串最少的分割字数
        初始化dp[0]则以空字符结尾,设置dp[0] = -1
        dp[1]则以第1个字符结尾，dp[1] = 0
        dp[2]则以第2个字符结尾，dp[2] = 1
        ...
        dp[i] = min(dp[j] + 1) (j < i & s[j:i]是回文)
        """
        n = len(s)
        dp = [i-1 for i in range(n+1)]
        f = lambda x: x == x[::-1]
        for i in range(1, n + 1):
            for j in range(i):
                if f(s[j:i]):
                    dp[i] = min(dp[j] + 1, dp[i])
        return dp[n]

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        f = [float("inf")] * n
        for i in range(n):
            if g[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if g[j + 1][i]:
                        f[i] = min(f[i], f[j] + 1)

        return f[n - 1]
# leetcode submit region end(Prohibit modification and deletion)
s = "aabbc"
print(Solution().minCut(s))