# 给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串： 
# 
#  
#  字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'） 
#  每个元音 'a' 后面都只能跟着 'e' 
#  每个元音 'e' 后面只能跟着 'a' 或者是 'i' 
#  每个元音 'i' 后面 不能 再跟着另一个 'i' 
#  每个元音 'o' 后面只能跟着 'i' 或者是 'u' 
#  每个元音 'u' 后面只能跟着 'a' 
#  
# 
#  由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 1
# 输出：5
# 解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
#  
# 
#  示例 2： 
# 
#  输入：n = 2
# 输出：10
# 解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。
#  
# 
#  示例 3： 
# 
#  输入：n = 5
# 输出：68 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2 * 10^4 
#  
#  Related Topics 动态规划 👍 135 👎 0
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp, mod = (1, 1, 1, 1, 1), 10 ** 9 + 7
        for _ in range(n - 1):
            dp = ((dp[1] + dp[2] + dp[4]) % mod, (dp[0] + dp[2]) % mod, (dp[1] + dp[3]) % mod, dp[2], (dp[2] + dp[3]) % mod)
        return sum(dp) % mod


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        f[n] = [[0 1 1 0 1]
                [1 0 1 0 0]
                [0 1 0 1 0]  X f[n - 1] = M X f[n - 1] = M^(n - 1) X f[1]
                [0 0 1 0 0]
                [0 0 1 1 0]]
        记矩阵为M
        f[n] = M^(n-1) X [1]
                         [1]
                         [1]
                         [1]
                         [1]
        使用快速幂求解，时间复杂度O(logn)
        """
        def multiply(a, b):
            res = [[0] * len(b[0]) for _ in range(len(a))]
            for i in range(len(a)):
                for j in range(len(b[0])):
                    for k in range(len(a[i])):
                        res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % mod
            return res

        def matrix_pow(matrix, n):
            res = [[1] for _ in range(len(matrix[0]))]
            while n:
                if n & 1: res = multiply(matrix, res)
                matrix = multiply(matrix, matrix)
                n >>= 1
            return res

        mod = 10 ** 9 + 7
        M = [[0, 1, 1, 0, 1],
             [1, 0, 1, 0, 0],
             [0, 1, 0, 1, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 1, 1, 0]]
        res = matrix_pow(M, n - 1)
        return sum(row[0] for row in res) % mod
# leetcode submit region end(Prohibit modification and deletion)
