# 有台奇怪的打印机有以下两个特殊要求： 
# 
#  
#  打印机每次只能打印由 同一个字符 组成的序列。 
#  每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。 
#  
# 
#  给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aaabbb"
# 输出：2
# 解释：首先打印 "aaa" 然后打印 "bbb"。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "aba"
# 输出：2
# 解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 100 
#  s 由小写英文字母组成 
#  
#  Related Topics 深度优先搜索 动态规划 
#  👍 124 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strangePrinter(self, s: str) -> int:
        """
        f(i, j) 为考虑区间[i, j]的最少打印次数
        考虑两种情况:
        1. s[i] == s[j], f(i, j) = f(i, j - 1)。因为在打印s[i]的时候可以把s[j]也一起打印了,
        2. s[i] != s[j], f(i, j) = min(f(i, k) + f(k + 1, j))   i <= k <= j - 1
        初始化： f[i][i] = 1，长度为1的区间，只需打印一次，最后答案为f[0][n-1]
        时间复杂度：O(n^3)
        """
        n = len(s)
        f = [[1000] * n for _ in range(n)]
        for i in range(n):
            f[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i][j-1]
                else:
                    for k in range(i, j):
                        f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j])
        return f[0][n-1]
# leetcode submit region end(Prohibit modification and deletion)
s = "aaabbb"
print(Solution().strangePrinter(s))