# 给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。 
# 
#  两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串： 
# 
#  
#  s = s1 + s2 + ... + sn 
#  t = t1 + t2 + ... + tm 
#  |n - m| <= 1 
#  交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ... 
#  
# 
#  提示：a + b 意味着字符串 a 和 b 连接。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：s1 = "", s2 = "", s3 = ""
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s1.length, s2.length <= 100 
#  0 <= s3.length <= 200 
#  s1、s2、和 s3 都由小写英文字母组成 
#  
#  Related Topics 字符串 动态规划 👍 598 👎 0
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3): return False
        f = [False] * (m + 1)
        f[0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                if i - 1 >= 0:
                    f[j] &= (s1[i - 1] == s3[i + j - 1])
                if j - 1 >= 0:
                    f[j] |= (f[j - 1] & (s2[j - 1] == s3[i + j - 1]))
        return f[m]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        f(i, j)表示s1前i个字符和s2前j个字符能否交错组成s3前i+j个字符
        f(i, j) = (f(i - 1, j) if s1[i - 1] == s3[i + j - 1]) or (f(i, j - 1) if s2[j - 1] == s3[i + j - 1])
        初始化f(0, 0) = True
        注意到f(i, j)只与上一行和这一行前一个的状态相关，所以空间复杂度可以优化
        """
        n, m = len(s1), len(s2)
        if n + m != len(s3): return False
        f = [[False] * (m + 1) for _ in range(n + 1)]
        f[0][0] = True
        for i in range(n + 1):
            for j in range(m + 1):
                if i - 1 >= 0 and s1[i - 1] == s3[i + j - 1]:
                    f[i][j] |= f[i - 1][j]
                if j - 1 >= 0 and s2[j - 1] == s3[i + j - 1]:
                    f[i][j] |= f[i][j - 1]
        return f[n][m]
# leetcode submit region end(Prohibit modification and deletion)
