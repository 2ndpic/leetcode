# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "a"
# 输出："a"
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "ac"
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母（大写和/或小写）组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 3728 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        f[i][j]表示考虑s[i,..j]是否为回文串。初始化f[i][i]=True,显然j>=i
        f[i][j] = f[i + 1][j - 1] & s[i] == s[j]
        """
        n = len(s)
        if n == 1: return s
        max_len = 1
        begin = 0
        f = [[False] * n for _ in range(n)]
        for i in range(n):
            f[i][i] = True
        for j in range(n):
            for i in range(j):
                if s[i] != s[j]:
                    f[i][j] = False
                elif j - i + 1 == 2:
                    f[i][j] = True
                else:
                    f[i][j] = f[i + 1][j - 1]

                if f[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]

# leetcode submit region end(Prohibit modification and deletion)
s = "bananas"
print(Solution().longestPalindrome(s))