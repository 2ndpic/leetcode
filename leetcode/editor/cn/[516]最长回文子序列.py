# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。 
# 
#  子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为 "bbbb" 。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出：2
# 解释：一个可能的最长回文子序列为 "bb" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由小写英文字母组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 565 👎 0
import functools
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @functools.lru_cache(None)
        def dfs(start, end):
            if start >= end: return 1 if start == end else 0
            if s[start] == s[end]: return 2 + dfs(start + 1, end - 1)
            return max(dfs(start, end - 1), dfs(start + 1, end))
        dfs.cache_clear()
        return dfs(0, len(s) - 1)
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        f[i][j]表示字符串s的下标范围[i,j]内的最长回文子序列的长度
        如果s[i]==s[j],则首先得到s下标[i + 1, j - 1]内的最长回文子序列，然后分别添加s[i]和s[j],则f[i][j] = f[i + 1][j - 1] + 2
        否则，s[i]和s[j]必不可能同时作为同一回文子序列的首尾，因此f[i][j] = max(f[i + 1][j], f[i][j - 1])
        """
        f = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            f[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]: f[i][j] = 2 + f[i + 1][j - 1]
                else: f[i][j] = max(f[i][j - 1], f[i + 1][j])
        return f[0][len(s) - 1]
# leetcode submit region end(Prohibit modification and deletion)
s = "abaa"
print(Solution().longestPalindromeSubseq(s))