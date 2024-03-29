# 可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
#  
#  'A'：Absent，缺勤 
#  'L'：Late，迟到 
#  'P'：Present，到场 
#  
# 
#  如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励： 
# 
#  
#  按 总出勤 计，学生缺勤（'A'）严格 少于两天。 
#  学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。 
#  
# 
#  给你一个整数 n ，表示出勤记录的长度（次数）。请你返回记录长度为 n 时，可能获得出勤奖励的记录情况 数量 。答案可能很大，所以返回对 109 + 7 
# 取余 的结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2
# 输出：8
# 解释：
# 有 8 种长度为 2 的记录将被视为可奖励：
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL" 
# 只有"AA"不会被视为可奖励，因为缺勤次数为 2 次（需要少于 2 次）。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：3
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 10101
# 输出：183236316
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 105 
#  
#  Related Topics 动态规划 
#  👍 179 👎 0
import functools
class Solution:
    def checkRecord(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(left, A = 1, L = 2):
            if left == 0: return 1
            ans = 0
            # 最后一天缺勤
            if A > 0:
                ans += dfs(left - 1, A - 1)
            # 最后一天迟到
            if L > 0:
                ans += dfs(left - 1, A, L - 1)
            # 最后一天出席
            ans += dfs(left - 1, A)
            return ans % (10 ** 9 + 7)
        dfs.cache_clear()
        return dfs(n)
class Solution:
    def checkRecord(self, n: int) -> int:
        """
        f[i][j][k]表示前i天有j个A且结尾有连续k个L的可奖励出勤记录的数量，0<=i<=n,0<=j<=1,0<=k<=2
        当i=0时，没有出勤记录，初始化f[0][0][0]=1
        当1<=i<=n时:
            当第i天正常出勤f[i][j][0] += sum(f[i - 1][j][k] for k in range(3))  (0<=j<=1)
            当第i天缺勤时  f[i][1][0] += sum(f[i-1][0][k] for k in range(3))
            当第i天迟到时  f[i][j][k] += f[i - 1][j][k - 1] (0<=j<=1, 1<=k<=2)
        最终答案为sum(f[n][][])
        """
        f = [[[0, 0, 0], [0, 0, 0]] for _ in range(n + 1)]
        f[0][0][0], mod = 1, 10 ** 9 + 7
        for i in range(1, n + 1):
            # P结尾
            for j in range(2):
                for k in range(3):
                    f[i][j][0] = (f[i][j][0] + f[i - 1][j][k]) % mod
            # A结尾
            for k in range(3):
                f[i][1][0] = (f[i][1][0] + f[i - 1][0][k]) % mod
            # L结尾
            for j in range(2):
                for k in range(1, 3):
                    f[i][j][k] = (f[i][j][k] + f[i - 1][j][k - 1]) % mod
        return sum(f[n][j][k] for j in range(2) for k in range(3)) % (10 ** 9 + 7)
class Solution:
    def checkRecord(self, n: int) -> int:
        """
        因为只与上一状态相关，优化空间复杂度O(1)
        """
        f = [[0, 0, 0], [0, 0, 0]]
        f[0][0], mod = 1, 10 ** 9 + 7
        for i in range(1, n + 1):
            # P结尾
            fn = [[0, 0, 0], [0, 0, 0]]
            for j in range(2):
                for k in range(3):
                    fn[j][0] = (fn[j][0] + f[j][k]) % mod
            # A结尾
            for k in range(3):
                fn[1][0] = (fn[1][0] + f[0][k]) % mod
            # L结尾
            for j in range(2):
                for k in range(1, 3):
                    fn[j][k] = (fn[j][k] + f[j][k - 1]) % mod
            f = fn
        return sum(f[j][k] for j in range(2) for k in range(3)) % mod
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkRecord(self, n: int) -> int:
        """
        矩阵快速幂
        f[i][j*3+k]来融合一个维度，表示前i天有j个A且结尾有连续k个L的数量，初始化自然是f[0][0]
        f[i][0] = f[i-1][0] + f[i-1][1] + f[i-1][2]
        f[i][1] = f[i-1][0]
        f[i][2] = f[i-1][1]
        f[i][3] = f[i-1][0] + f[i-1][1] + f[i-1][2] + f[i-1][3] + f[i-1][4] + f[i-1][5]
        f[i][4] = f[i-1][3]
        f[i][5] = f[i-1][4]
        令f[n]表示包含6个元素的行向量：f[n] = [f[n][0], f[n][1],...,f[n][5]]
        f[n] = f[n-1] * M
               其中  M = [1 1 0 1 0 0]
                        [1 0 1 1 0 0]
                        [1 0 0 1 0 0]
                        [0 0 0 1 1 0]
                        [0 0 0 1 0 1]
                        [0 0 0 1 0 0]
        因此f[n] = f[0] * (M^n)
        f[0] = (1, 0, 0, 0, 0, 0)
        """
        def multiply(A, B):
            r, c = len(A), len(B[0])
            ret = [[0] * c for _ in range(r)]
            for i in range(r):
                for j in range(c):
                    for k in range(len(A[0])):
                        ret[i][j] += A[i][k] * B[k][j]
                        ret[i][j] %= mod
            return ret
        def matrix_pow(mat, n):
            ret = [[1, 0, 0, 0, 0, 0]]
            while n > 0:
                if n & 1:
                    ret = multiply(ret, mat)
                mat = multiply(mat, mat)
                n >>= 1
            return ret

        mod = (10 ** 9 + 7)
        M = [[1, 1, 0, 1, 0, 0],
             [1, 0, 1, 1, 0, 0],
             [1, 0, 0, 1, 0, 0],
             [0, 0, 0, 1, 1, 0],
             [0, 0, 0, 1, 0, 1],
             [0, 0, 0, 1, 0, 0]]
        res = matrix_pow(M, n)
        return sum(res[0]) % mod


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().checkRecord(100))