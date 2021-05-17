# 有 n 根长度互不相同的木棍，长度为从 1 到 n 的整数。请你将这些木棍排成一排，并满足从左侧 可以看到 恰好 k 根木棍。从左侧 可以看到 木棍的前提是
# 这个木棍的 左侧 不存在比它 更长的 木棍。 
# 
#  
#  例如，如果木棍排列为 [1,3,2,5,4] ，那么从左侧可以看到的就是长度分别为 1、3 、5 的木棍。 
#  
# 
#  给你 n 和 k ，返回符合题目要求的排列 数目 。由于答案可能很大，请返回对 109 + 7 取余 的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 3, k = 2
# 输出：3
# 解释：[1,3,2], [2,3,1] 和 [2,1,3] 是仅有的能满足恰好 2 根木棍可以看到的排列。
# 可以看到的木棍已经用粗体+斜体标识。
#  
# 
#  示例 2： 
# 
#  输入：n = 5, k = 5
# 输出：1
# 解释：[1,2,3,4,5] 是唯一一种能满足全部 5 根木棍可以看到的排列。
# 可以看到的木棍已经用粗体+斜体标识。
#  
# 
#  示例 3： 
# 
#  输入：n = 20, k = 11
# 输出：647427950
# 解释：总共有 647427950 (mod 109 + 7) 种能满足恰好有 11 根木棍可以看到的排列。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 1000 
#  1 <= k <= n 
#  
#  Related Topics 动态规划 
#  👍 22 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        """
        f[i][j]表示用长度递增的i根棍子看到j根的方案数
        初始化：f[0][0] = 1, f[0][i] = 0 if i != 0
        - 能看到最后一根，则最后一根必为长度为i的棍子, f[i-1][j-1]
        - 不能看到最后一根，最后一根为[1,..,i-1]的任一可能，若为x，则前i-1根棍子排列为[1,...,x-1,x+1,..i],则方案数为f[i-1][j]
        f[i][j] = f[i-1][j-1] + (i - 1) * f[i-1][j]
        """
        mod = 10 ** 9 + 7
        # f = [[0] * (k + 1) for _ in range(2)]
        # f[0][0] = 1
        # for i in range(1, n + 1):
        #     for j in range(1, k + 1):
        #         f[i & 1][j] = ((i - 1) * f[(i - 1) & 1][j] + f[(i - 1) & 1][j - 1]) % mod
        # return f[n & 1][k]
        f = [1] + [0] * k
        for i in range(1, n + 1):
            g = [0] * (k + 1)
            for j in range(1, k + 1):
                g[j] = (f[j-1] + (i - 1) * f[j]) % mod
            f = g
        return f[k]


# leetcode submit region end(Prohibit modification and deletion)
n = 20; k = 11
n = 5; k = 5
print(Solution().rearrangeSticks(n, k))