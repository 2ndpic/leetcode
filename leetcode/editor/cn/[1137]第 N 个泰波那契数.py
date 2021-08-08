# 泰波那契序列 Tn 定义如下： 
# 
#  T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2 
# 
#  给你整数 n，请返回第 n 个泰波那契数 Tn 的值。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 4
# 输出：4
# 解释：
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#  
# 
#  示例 2： 
# 
#  输入：n = 25
# 输出：1389537
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 37 
#  答案保证是一个 32 位整数，即 answer <= 2^31 - 1。 
#  
#  Related Topics 记忆化搜索 数学 动态规划 
#  👍 111 👎 0
class Solution:
    def tribonacci(self, n: int) -> int:
        a  = [0, 1, 1]
        if n < 3:
            return a[n]
        for _ in range(n - 2):
            a[0], a[1], a[2] = a[1], a[2], a[0] + a[1] + a[2]
        return a[2]

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def tribonacci(self, n: int) -> int:
        def multiply(a, b):
            assert len(a[0]) == len(b), f"{len(a[0])} {len(b)} shapes not aligned"
            c = [[0] * len(b[0]) for _ in range(len(a))]
            for i in range(len(a)):
                for j in range(len(b[0])):
                    c[i][j] = sum(a[i][k] * b[k][j] for k in range(len(a[0])))
            return c

        def matrix_pow(a, k):
            ret = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            while k > 0:
                if k & 1: ret = multiply(a, ret)
                k >>= 1
                a = multiply(a, a)
            return ret

        res = matrix_pow([[1, 1, 1], [1, 0, 0], [0, 1, 0]], n)
        res = multiply(res, [[1], [1], [0]])
        return res[2][0]
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().tribonacci(25))